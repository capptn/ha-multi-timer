async function load() {
 const entities = await fetch("/api/entities").then(r=>r.json());
 entity.innerHTML = entities.map(e=>`<option>${e}</option>`).join("");
 const programs = await fetch("/api/programs").then(r=>r.json());
 list.innerHTML = programs.map(p=>`<li>${p.time} → ${p.entity}</li>`).join("");
}
async function add() {
 await fetch("/api/programs",{method:"POST",headers:{"Content-Type":"application/json"},
 body:JSON.stringify({entity:entity.value,time:time.value,service:service.value})});
 load();
}
load();
