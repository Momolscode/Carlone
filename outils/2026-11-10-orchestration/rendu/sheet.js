const fs=require('fs'),path=require('path');const {chromium}=require('playwright');
(async()=>{const dir=process.argv[2];const ids=process.argv[3].split(',');const cols=+process.argv[4]||3;const w=+process.argv[5]||640;const out=process.argv[6];
const h=Math.round(w*9/16);
const html='<html><body style="margin:0;background:#222;display:grid;grid-template-columns:repeat('+cols+','+w+'px);gap:6px;padding:6px;width:'+(cols*w+(cols-1)*6)+'px">'+ids.map(id=>'<div style="position:relative"><img src="data:image/png;base64,'+fs.readFileSync(path.join(dir,id+'.png')).toString('base64')+'" style="width:'+w+'px;height:'+h+'px;display:block"><span style="position:absolute;left:4px;top:4px;background:#000;color:#fff;font:12px sans-serif;padding:2px 5px">'+id+'</span></div>').join('')+'</body></html>';
const b=await chromium.launch();const p=await b.newPage({viewport:{width:cols*w+(cols+1)*6,height:800}});await p.setContent(html);await p.screenshot({path:out,fullPage:true});await b.close()})()
