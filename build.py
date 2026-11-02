"""Wrap src/app.html (artifact-style fragment) into a full document at index.html."""
from pathlib import Path

root = Path(__file__).parent
src = (root / "src" / "app.html").read_text()
split = src.index('<div class="wrap">')
head, body = src[:split], src[split:]

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Pomodoro timer with an Eisenhower matrix and binaural beats.">
<style>
:root {{ color-scheme: light; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }}
body {{ margin: 0; font: 14px system-ui, sans-serif; }}
img {{ max-width: 100%; }}
[hidden] {{ display: none !important; }}
</style>
{head.strip()}
</head>
<body>
{body.strip()}
</body>
</html>
"""
(root / "index.html").write_text(page)
print(f"wrote index.html ({len(page):,} bytes)")
