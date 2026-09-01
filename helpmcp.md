# Agent playbook: install Grounded Docs (Docs MCP Server) on Linux

Use this when installing [arabold/docs-mcp-server](https://github.com/arabold/docs-mcp-server) (`@arabold/docs-mcp-server`, MIT) as a local replacement for Cursor `@Docs`.

Goal: a long-running local server on **127.0.0.1:6280** (web UI + MCP), surviving logout, with **Ollama `nomic-embed-text`** for vector search. Cursor MCP URL: `http://127.0.0.1:6280/mcp`.

Do **not** use Firecrawl. Do **not** `npx` with system Node 18. Do **not** start the server until Playwright Chromium is installed **without** `--with-deps`. Do **not** skip linger or embeddings — both are part of a complete install.

This is a **shadow MCP** (local HTTP, not Runlayer). Warn the human once, then continue if they asked to install it.

Proven on Ubuntu Noble: apt Node 18, no Docker, Node 22 tarball in `~/.local/opt/node-22`, systemd user unit `grounded-docs`, system unit `ollama.service`.

---

## 0. Success criteria (stop when all true)

1. `curl -sS -o /dev/null -w '%{http_code}\n' http://127.0.0.1:6280/` prints `200`
2. `docs-mcp-server list` runs (empty `[]` is OK)
3. Cursor MCP has `docs-mcp-server` → `http://127.0.0.1:6280/mcp`
4. `loginctl show-user "$USER" -p Linger` prints `Linger=yes`
5. `systemctl is-active ollama` is `active` and `curl -sf http://127.0.0.1:11434/api/version` works
6. `docs-mcp-server config --output json` shows `"embeddingModel": "openai:nomic-embed-text"`
7. Tell the human: open **http://127.0.0.1:6280**, add a docs URL, then reload MCP in Cursor Settings → MCP

Do not scrape/index docs unless they asked. Libraries indexed **before** embeddings was enabled still have full-text only until refresh/re-scrape.

---

## 1. Probe first (read-only)

```bash
uname -s
command -v docker; docker info >/dev/null 2>&1 && echo docker-ok || echo docker-missing
node -v 2>/dev/null || echo no-node
command -v ss >/dev/null && ss -ltn | grep -E '6280|11434' || echo 'ports 6280/11434 check done'
command -v systemctl >/dev/null && systemctl --user status >/dev/null && echo systemd-user-ok
systemctl is-active ollama 2>/dev/null || echo ollama-not-active
command -v ollama; ollama list 2>/dev/null | head
loginctl show-user "$USER" -p Linger 2>/dev/null || true
python3 -c "import json,pathlib; p=pathlib.Path.home()/'.cursor'/'mcp.json'; print('user mcp', sorted(json.loads(p.read_text()).get('mcpServers',{})) if p.exists() else 'none')"
```

Also check project `.cursor/mcp.json` the same way (**print keys only**, never dump the file; it may contain tokens).

Pick a path:

| Condition | Path |
|---|---|
| Docker daemon works | **A — Docker** (fastest for the server; still wire Ollama on the host) |
| No Docker, Node `v22+` on PATH | **B — npm global + systemd** |
| No Docker, Node `< 22` or missing | **C — install Node 22 into `~/.local/opt`, then B** |

Ubuntu apt Node (Noble) is **18**. That is not enough. `nix-env -qaP nodejs_*` can hang for minutes and still return nothing — do not wait on it.

Do **§Ollama + linger** (section 6) on every path before calling the install done.

---

## 2. Path A — Docker (preferred if the daemon works)

```bash
docker run -d --name grounded-docs --restart unless-stopped \
  -p 127.0.0.1:6280:6280 \
  -v docs-mcp-data:/data \
  -v docs-mcp-config:/config \
  -e OPENAI_API_KEY=ollama \
  -e OPENAI_API_BASE=http://host.docker.internal:11434/v1 \
  -e DOCS_MCP_EMBEDDING_MODEL=openai:nomic-embed-text \
  --add-host=host.docker.internal:host-gateway \
  ghcr.io/arabold/docs-mcp-server:latest \
  --protocol http --host 0.0.0.0 --port 6280 \
  --embedding-model openai:nomic-embed-text --telemetry false
```

Host Ollama must already listen on `127.0.0.1:11434` (section 6). If Docker cannot reach it, fall back to Path B.

Wait until `curl http://127.0.0.1:6280/` is 200, then **§5 MCP config** and **§6**.

If `docker` is absent or the daemon is down, use Path C/B. Do not install Docker unless the human asked.

---

## 3. Path C — Node 22 in home (when system Node is 18)

Do **not** overwrite `/usr/bin/node`. Install a private prefix.

```bash
set -euo pipefail
VER=$(python3 - <<'PY'
import json, urllib.request
with urllib.request.urlopen('https://nodejs.org/dist/index.json', timeout=30) as r:
    data = json.load(r)
for rel in data:
    if rel['version'].lstrip('v').startswith('22.'):
        print(rel['version']); break
else:
    raise SystemExit('no v22')
PY
)
TARBALL="node-${VER}-linux-x64.tar.xz"
mkdir -p "$HOME/.local/opt" "$HOME/.local/bin" /tmp/node-install
cd /tmp/node-install
curl -fsSL -o "$TARBALL" "https://nodejs.org/dist/${VER}/${TARBALL}"
tar -xJf "$TARBALL"
DEST="$HOME/.local/opt/node-${VER}"
rm -rf "$DEST"
mv "node-${VER}-linux-x64" "$DEST"
ln -sfn "$DEST" "$HOME/.local/opt/node-22"
for b in node npm npx; do ln -sfn "$DEST/bin/$b" "$HOME/.local/bin/$b"; done
export PATH="$HOME/.local/opt/node-22/bin:$PATH"
node -v   # must be v22.x
```

Keep using `export PATH="$HOME/.local/opt/node-22/bin:$PATH"` for every later npm/docs-mcp command. Cursor sandboxes and login shells may still see system Node 18.

---

## 4. Path B — package, Playwright, systemd

### 4.1 Install the CLI **before** starting the server

```bash
export PATH="$HOME/.local/opt/node-22/bin:$PATH"   # skip if system node is already 22+
npm install -g @arabold/docs-mcp-server@latest
command -v docs-mcp-server
ln -sfn "$(command -v docs-mcp-server)" "$HOME/.local/bin/docs-mcp-server"
docs-mcp-server --help | head
```

`--help` is a yargs command list. `docs-mcp-server` with no args starts the **server** (can hang a `head` pipe). Prefer `docs-mcp-server --help`. Binary name: **`docs-mcp-server`**.

Set the embedding model in config **before** the first index (avoids a later non-interactive systemd crash on model change):

```bash
docs-mcp-server config set app.embeddingModel openai:nomic-embed-text
docs-mcp-server config set app.telemetryEnabled false
```

The generated YAML default is `text-embedding-3-small` (OpenAI). Overwrite it. `nomic-embed-text` is **768** dimensions; do not force 1536.

### 4.2 Playwright — do this **before** first `server` start

On first launch the package runs:

```text
npm exec -y playwright install --no-shell --with-deps chromium
```

`--with-deps` wants **sudo apt** and **hangs** with no useful journal. Cursor agent sandboxes also send the browser zip to `/tmp/cursor-sandbox-cache/...`, which the systemd service cannot see, so the next start tries `--with-deps` again.

**Fix, in this order:**

1. Never start `docs-mcp-server server` until Chromium exists in a **stable home path**.
2. Install **without** `--with-deps`, with an explicit browsers dir, **outside** a network-restricted sandbox if the download stalls:

```bash
export PATH="$HOME/.local/opt/node-22/bin:$PATH"
export PLAYWRIGHT_BROWSERS_PATH="$HOME/.cache/ms-playwright"
mkdir -p "$PLAYWRIGHT_BROWSERS_PATH"
cd "$(npm root -g)/@arabold/docs-mcp-server"
npx playwright install --no-shell chromium
CHROME=$(find "$PLAYWRIGHT_BROWSERS_PATH" -type f -name chrome -path '*chrome-linux64/*' | head -1)
test -x "$CHROME"
echo "$CHROME"
```

If the zip landed in `/tmp/cursor-sandbox-cache/.../playwright/`, copy it:

```bash
cp -a /tmp/cursor-sandbox-cache/*/playwright/. "$HOME/.cache/ms-playwright/"
```

3. Skip auto-install at runtime (`PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1`) **and** set `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH` to that `chrome` binary. The skip env is what actually prevents the sudo hang.

JS-heavy / hash-routed docs sites need Chromium. Plain fetch scrapes still work without it, but the stock startup script will stall unless skip/path is set.

### 4.3 systemd user service (Linux desktop)

Complete **§6** first if Ollama is not already `active` on `:11434`.

```bash
mkdir -p "$HOME/.local/share/docs-mcp-server" "$HOME/.config/systemd/user"
```

Write `$HOME/.config/systemd/user/grounded-docs.service`. Substitute `USER` and the real `chrome` path from 4.2. This is the unit that worked:

```ini
[Unit]
Description=Grounded Docs MCP Server
After=network.target

[Service]
Type=simple
ExecStartPre=/usr/bin/curl -sf --retry 30 --retry-delay 1 --retry-all-errors http://127.0.0.1:11434/api/version
ExecStart=/home/USER/.local/opt/node-22/bin/docs-mcp-server server --protocol http --host 127.0.0.1 --port 6280 --store-path /home/USER/.local/share/docs-mcp-server --telemetry false --embedding-model openai:nomic-embed-text
Restart=on-failure
RestartSec=3
Environment=HOME=/home/USER
Environment=PATH=/home/USER/.local/opt/node-22/bin:/usr/bin:/bin
Environment=PLAYWRIGHT_BROWSERS_PATH=/home/USER/.cache/ms-playwright
Environment=PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH=/home/USER/.cache/ms-playwright/chromium-XXXX/chrome-linux64/chrome
Environment=PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
Environment=OPENAI_API_KEY=ollama
Environment=OPENAI_API_BASE=http://127.0.0.1:11434/v1
Environment=DOCS_MCP_EMBEDDING_MODEL=openai:nomic-embed-text

[Install]
WantedBy=default.target
```

Use the **absolute** Node-22 `docs-mcp-server` in `ExecStart`. Bind **127.0.0.1**, not `0.0.0.0`. A user unit cannot reliably `After=ollama.service` (Ollama is a **system** unit); `ExecStartPre` curl is the boot-race fix.

If system Node is already 22+, `ExecStart` can be the path from `command -v docs-mcp-server`.

```bash
systemctl --user daemon-reload
systemctl --user enable --now grounded-docs.service
loginctl enable-linger "$USER"
loginctl show-user "$USER" -p Linger   # must be Linger=yes
```

If `enable` says the unit does not exist, the file was written after `daemon-reload` — reload again and retry.

Linger is **required**. Without it, `grounded-docs` dies on logout. `loginctl enable-linger` is a persistent account setting; the human asked for it on this project. Ollama as a system unit already survives logout; linger only covers the user unit.

No systemd user session → `nohup` with the same env/flags, still bound to 127.0.0.1:6280 (will not survive logout).

Wait until the port is up (Playwright skip should make this a few seconds):

```bash
for i in $(seq 1 20); do ss -ltn | grep -q 6280 && break; sleep 1; done
curl -sS -o /dev/null -w '%{http_code}\n' http://127.0.0.1:6280/
```

`200` = UI is up. `GET /mcp` returning **405** is normal (Streamable HTTP wants POST). `GET /sse` may 200.

If journal shows another `playwright install --with-deps`, stop the unit and fix env/chrome path before starting again.

If the unit fails immediately with an embedding-model-change error: systemd has no TTY, so the server will not prompt. Start once in a real terminal to confirm, or set the model **before** the first index (4.1).

---

## 5. Cursor MCP config

Merge into `~/.cursor/mcp.json` (all workspaces) **and/or** the project `.cursor/mcp.json`. Preserve existing servers. Print **keys only**.

```json
"docs-mcp-server": {
  "url": "http://127.0.0.1:6280/mcp"
}
```

That matches current Cursor HTTP MCP (same shape as Context7). Official docs also allow `"type": "streamableHttp"`. Do **not** use stdio `npx` with Node 18.

Tell the human to reload MCP. Then they add sources in the UI or:

```bash
docs-mcp-server scrape <library-name> https://example.com/docs
```

---

## 6. Ollama (required for embeddings)

Do this before declaring success. Prefer the **system** service, not a one-off `ollama serve` in a terminal.

```bash
command -v ollama
systemctl is-active ollama || sudo systemctl enable --now ollama
curl -sf http://127.0.0.1:11434/api/version
ollama pull nomic-embed-text
ollama list | grep nomic-embed-text
```

Only `sudo` for `enable --now` if the unit exists and is inactive. If Ollama is not installed, stop and ask the human — do not invent a cloud OpenAI key.

Smoke-test embeddings (expect dimension 768):

```bash
curl -sf http://127.0.0.1:11434/api/embeddings \
  -H 'Content-Type: application/json' \
  -d '{"model":"nomic-embed-text","prompt":"ping"}' \
  | python3 -c 'import sys,json; print(len(json.load(sys.stdin).get("embedding") or []))'
```

Grounded Docs talks to Ollama as an OpenAI-compatible endpoint: `OPENAI_API_KEY=ollama`, `OPENAI_API_BASE=http://127.0.0.1:11434/v1`, model `openai:nomic-embed-text`.

From Docker, use `http://host.docker.internal:11434/v1` plus `--add-host=host.docker.internal:host-gateway`.

Config file: `~/.config/docs-mcp-server/config.yaml`. **Set `embeddings.vectorDimension: 768` explicitly** and `DOCS_MCP_EMBEDDINGS_VECTOR_DIMENSION=768` on the systemd unit. The generated default is **1536** (OpenAI). If you omit it, sqlite-vec keeps `FLOAT[1536]` while nomic queries are 768, and `search_docs` dies with `Dimension mismatch ... Expected 1536 ... received 768`.

After changing the model/dimension, **`refresh` is not enough** (it skips unchanged pages, so NULL embeddings stay). Recrawl with scrape (`clean` defaults to true):

```bash
docs-mcp-server scrape 'ovn wiki' 'https://ovn.world/index.php?title=Main_Page' \
  --scope hostname --max-pages 2000 --max-depth 5
```

Or use the MCP `scrape_docs` tool with the same limits. Check vectors with `SELECT COUNT(*) FROM documents WHERE embedding IS NOT NULL` on `~/.local/share/docs-mcp-server/documents.db`.

Data: `~/.local/share/docs-mcp-server/`.

Upstream: [embedding models](https://github.com/arabold/docs-mcp-server/blob/main/docs/guides/embedding-models.md).

---

## 7. Failure table (what we actually hit)

| Symptom | Cause | Fix |
|---|---|---|
| `EBADENGINE` / package wants Node 22 | apt Node 18 | Path C |
| `nix-env -qaP` hangs / empty | no useful nodejs_22 from that query | skip Nix; official tarball |
| Server “active” but nothing on 6280 | first-start Playwright `--with-deps` waiting on sudo | skip download + set chrome path; install chromium without `--with-deps` |
| Chromium in `/tmp/cursor-sandbox-cache/...` | agent sandbox cache | copy into `~/.cache/ms-playwright` |
| `enable`: unit file does not exist | race: write vs `daemon-reload` | reload, then enable |
| UI 200, Cursor cannot see tools | MCP not reloaded, or used `/sse` vs `/mcp` | use `/mcp`; reload MCP |
| `GET /mcp` → 405 | expected | ignore |
| Service gone after logout | systemd Linger=no | `loginctl enable-linger $USER` |
| Unit fails: embedding model change | systemd has no TTY | set model before first index, or confirm once in a TTY |
| Config still `text-embedding-3-small` | generated OpenAI default | `docs-mcp-server config set app.embeddingModel openai:nomic-embed-text` |
| `search_docs` Dimension mismatch Expected 1536 received 768 | vec table built at OpenAI default 1536; nomic is 768 | set `embeddings.vectorDimension: 768`, restart, then **scrape** (not refresh) |
| `could not connect` to Ollama during probe | sandbox or Ollama down | `systemctl is-active ollama`; curl `:11434` with full permissions |
| Docker path skipped | no docker binary/daemon | Path C/B |

Useful logs:

```bash
systemctl --user status grounded-docs
journalctl --user -u grounded-docs -n 50 --no-pager
systemctl status ollama --no-pager | head
ps --forest -g "$(systemctl --user show -p MainPID --value grounded-docs)" -o pid,etime,cmd
```

---

## 8. What not to do

- Do not `npm install -g` with `/usr/bin/node` v18
- Do not `npx @arabold/docs-mcp-server@latest` as the long-running process on Node 18
- Do not run `playwright install --with-deps` (sudo trap)
- Do not bind `0.0.0.0` unless the human asked for LAN access
- Do not dump `mcp.json` (secrets)
- Do not wait more than ~30s for 6280 on a **fresh** start if Playwright skip is set; if it is installing chromium, stop and apply §4.2
- Do not treat empty `docs-mcp-server list` as failure
- Do not skip `loginctl enable-linger` (user asked for always-on)
- Do not omit `embeddings.vectorDimension` when using nomic (generated default is 1536)
- Do not use `refresh` to rebuild vectors; recrawl with `scrape` (`clean` defaults to true)
- Do not leave embeddings off or pointed at OpenAI when Ollama is available
- Do not add a paid OpenAI key unless the human asked

Upstream: https://github.com/arabold/docs-mcp-server — `docs/setup/installation.md` and `docs/guides/mcp-clients.md`.
