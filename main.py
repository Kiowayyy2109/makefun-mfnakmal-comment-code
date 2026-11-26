import os

LINE = "// This works. Nobody knows why. If you touch it, it stops working, and so do I."

LIMIT = 200
if len(LINE) != 80 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 80 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

# The comment is the warning label the fragile code deserves.
