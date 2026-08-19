# Agent playbook: install Grounded Docs (Docs MCP Server) on Linux

Use this when installing [arabold/docs-mcp-server](https://github.com/arabold/docs-mcp-server) (`@arabold/docs-mcp-server`, MIT) as a local replacement for Cursor `@Docs`.

Goal: a long-running local server on **127.0.0.1:6280** with a web UI, plus Cursor MCP pointed at `http://127.0.0.1:6280/mcp`.

Do **not** use Firecrawl. Do **not** `npx` with system Node 18. Do **not** start the server until Playwright Chromium is installed **without** `--with-deps`.

This is a **shadow MCP** (local HTTP, not Runlayer). Warn the human once, then continue if they asked to install it.

---

## 0. Success criteria (stop when all true)

1. `curl -sS -o /dev/null -w '%{http_code}\n' http://127.0.0.1:6280/` prints `200`
2. `docs-mcp-server list` runs (empty `[]` is OK)
3. Cursor MCP has `docs-mcp-server` → `http://127.0.0.1:6280/mcp`
4. Tell the human: open **http://127.0.0.1:6280**, add a docs URL, then reload MCP in Cursor Settings → MCP

Do not scrape/index docs unless they asked.

---

## 1. Probe first (read-only)

Run these before installing anything:

```bash
uname -s
command -v docker; docker info >/dev/null 2>&1 && echo docker-ok || echo docker-missing
node -v 2>/dev/null || echo no-node
command -v ss >/dev/null && ss -ltn | grep 6280 || echo 'port 6280 free'
command -v systemctl >/dev/null && systemctl --user status >/dev/null && echo systemd-user-ok
python3 -c "import json,pathlib; p=pathlib.Path.home()/'.cursor'/'mcp.json'; print('user mcp', sorted(json.loads(p.read_text()).get('mcpServers',{})) if p.exists() else 'none')"
```

Also check project `.cursor/mcp.json` the same way (**print keys only**, never dump the file; it may contain tokens).

Pick a path:

| Condition | Path |
|---|---|
| Docker daemon works | **A — Docker** (fastest, skip Node/Playwright pain) |
| No Docker, Node `v22+` on PATH | **B — npm global + systemd** |
| No Docker, Node `< 22` or missing | **C — install Node 22 into `~/.local/opt`, then B** |

Ubuntu apt Node (Noble) is **18**. That is not enough. `nix-env -qaP nodejs_*` can hang for minutes and still return nothing — do not wait on it.

---

## 2. Path A — Docker (preferred)

```bash
docker run -d --name grounded-docs --restart unless-stopped \
  -p 127.0.0.1:6280:6280 \
  -v docs-mcp-data:/data \
  -v docs-mcp-config:/config \
  ghcr.io/arabold/docs-mcp-server:latest \
  --protocol http --host 0.0.0.0 --port 6280
```

Wait until `curl http://127.0.0.1:6280/` is 200, then jump to **§5 MCP config**.

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

## 4. Path B — package, Playwright, then server

### 4.1 Install the CLI **before** starting the server

```bash
export PATH="$HOME/.local/opt/node-22/bin:$PATH"   # skip if system node is already 22+
npm install -g @arabold/docs-mcp-server@latest
command -v docs-mcp-server
ln -sfn "$(command -v docs-mcp-server)" "$HOME/.local/bin/docs-mcp-server"
docs-mcp-server --help | head
```

`--help` is a yargs command list. `docs-mcp-server` with no args starts the **server** (can hang a `head` pipe). Prefer `docs-mcp-server --help`. Binary name: **`docs-mcp-server`**.

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

JS-heavy / hash-routed docs sites need Chromium. Plain fetch scrapes still work without it, but the stock startup script will exit or stall unless skip/path is set.

### 4.3 systemd user service (Linux desktop)

```bash
mkdir -p "$HOME/.local/share/docs-mcp-server" "$HOME/.config/systemd/user"
```

Write `$HOME/.config/systemd/user/grounded-docs.service` (substitute the real chrome path from step 4.2):

```ini
[Unit]
Description=Grounded Docs MCP Server
After=network.target

[Service]
Type=simple
ExecStart=/home/USER/.local/opt/node-22/bin/docs-mcp-server server --protocol http --host 127.0.0.1 --port 6280 --store-path /home/USER/.local/share/docs-mcp-server --telemetry false
Restart=on-failure
RestartSec=3
Environment=HOME=/home/USER
Environment=PATH=/home/USER/.local/opt/node-22/bin:/usr/bin:/bin
Environment=PLAYWRIGHT_BROWSERS_PATH=/home/USER/.cache/ms-playwright
Environment=PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH=/home/USER/.cache/ms-playwright/chromium-XXXX/chrome-linux64/chrome
Environment=PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1

[Install]
WantedBy=default.target
```

Use the **absolute** Node-22 `docs-mcp-server` in `ExecStart`. Bind **127.0.0.1**, not `0.0.0.0`.

If system Node is already 22+, `ExecStart` can be `.../bin/docs-mcp-server` from `command -v docs-mcp-server`.

```bash
systemctl --user daemon-reload
systemctl --user enable --now grounded-docs.service
```

If `enable` says the unit does not exist, the file was written after `daemon-reload` — reload again and retry.

`loginctl show-user $USER -p Linger` is often `Linger=no`: the service **dies on logout**. Mention that. Only run `loginctl enable-linger $USER` if the human wants it.

No systemd user session → `nohup` with the same env/flags, still bound to 127.0.0.1:6280.

Wait until the port is up (Playwright skip should make this a few seconds, not minutes):

```bash
for i in $(seq 1 20); do ss -ltn | grep -q 6280 && break; sleep 1; done
curl -sS -o /dev/null -w '%{http_code}\n' http://127.0.0.1:6280/
```

`200` = UI is up. `GET /mcp` returning **405** is normal (Streamable HTTP wants POST). `GET /sse` may 200.

If journal shows another `playwright install --with-deps`, stop the unit and fix env/chrome path before starting again.

---

## 5. Cursor MCP config

Merge into `~/.cursor/mcp.json` (all workspaces) **and/or** the project `.cursor/mcp.json`. Preserve existing servers. Print **keys only**.

```json
"docs-mcp-server": {
  "url": "http://127.0.0.1:6280/mcp"
}
```

That matches current Cursor HTTP MCP (same shape as Context7). Official docs also allow `"type": "streamableHttp"`. Do **not** use stdio `npx` with Node 18.

Tell the human to reload MCP. Index is empty until they add sources in the UI or:

```bash
docs-mcp-server scrape <library-name> https://example.com/docs
```

---

## 6. Optional embeddings (later)

Search works without embeddings (worse quality). Do not add OpenAI keys unless asked.

Ollama (`nomic-embed-text`) is the free local option. Only configure it if `ollama serve` is actually running. See upstream [embedding models](https://github.com/arabold/docs-mcp-server/blob/main/docs/guides/embedding-models.md).

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
| Service gone after logout | systemd Linger=no | start again, or enable linger |
| Docker path skipped | no docker binary/daemon | Path C/B |

Useful logs:

```bash
systemctl --user status grounded-docs
journalctl --user -u grounded-docs -n 50 --no-pager
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

Upstream: https://github.com/arabold/docs-mcp-server — install + Cursor notes in `docs/setup/installation.md` and `docs/guides/mcp-clients.md`.
