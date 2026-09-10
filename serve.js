const http = require("http"), fs = require("fs"), path = require("path"), url = require("url");
const ROOT = __dirname;   /* 이 파일이 있는 폴더를 통째로 내보낸다 */
const MIME = {".html":"text/html; charset=utf-8",".js":"text/javascript",".css":"text/css",
  ".png":"image/png",".jpg":"image/jpeg",".webp":"image/webp",".md":"text/plain; charset=utf-8"};

http.createServer((req, res) => {
  const u = url.parse(req.url, true);
  const p = decodeURIComponent(u.pathname);
  res.setHeader("Access-Control-Allow-Origin", "*");

  if (req.method === "POST" && p === "/_save") {
    const rel = u.query.p || "";
    const full = path.resolve(ROOT, rel);
    if (!full.startsWith(ROOT)) { res.writeHead(403); return res.end("out of root"); }
    const chunks = [];
    req.on("data", c => chunks.push(c));
    req.on("end", () => {
      try {
        fs.mkdirSync(path.dirname(full), { recursive: true });
        const buf = Buffer.concat(chunks);
        fs.writeFileSync(full, buf);
        res.end("saved " + rel + " " + buf.length);
      } catch (e) { res.writeHead(500); res.end("ERR " + e.message); }
    });
    return;
  }
  if (p === "/") { res.setHeader("Content-Type", MIME[".html"]);
    return res.end("<!doctype html><meta charset=utf-8><title>uch tool</title><body>ready"); }

  const f = path.resolve(ROOT, "." + p);
  if (!f.startsWith(ROOT) || !fs.existsSync(f) || !fs.statSync(f).isFile()) {
    res.writeHead(404); return res.end("not found");
  }
  const ct = MIME[path.extname(f).toLowerCase()];
  if (ct) res.setHeader("Content-Type", ct);
  res.end(fs.readFileSync(f));
}).listen(8788, () => console.log("serving " + ROOT + " on http://localhost:8788/"));
