#consultas cypher

#1. Listar todos los Targaryen y sus apodos
MATCH (t:Personaje) 
WHERE t.nombre CONTAINS "Targaryen" 
RETURN t.nombre, t.apodo

# 2. Mostrar el árbol genealógico de los Targaryen
MATCH (p1:Personaje)-[:Padre]->(p2:Personaje)
RETURN p1.nombre AS Progenitor, p2.nombre AS Descendiente

#3. Mostrar una lista de los distintos tipos de lugares
MATCH (l)
WHERE  (l:bahia OR l:mar OR l:castillo OR l:ciudad OR l:continente OR l:isla OR l:region)
RETURN l.nombre AS Nombre, labels(l) AS Tipo

#4. para obtener el grafo que indica las relaciones sobre donde se ubica cada lugar
MATCH p=()-[:ubicado_en]->() RETURN p;

# 5.Mostrar los dragones
MATCH (n:Dragon) 
RETURN n.nombre as nombre, n.genero as genero, n.apodo as apodo ,n.color as color,n.ojos as ojos,n.nacimiento as nacimiento, n.muerte as muerte


#6. Mostrar los jinetes de dragón
MATCH p=()-[:Jinete]->() RETURN p;

#7. ¿Quiénes son los Targaryen que vivieron durante el Siglo Sangriento?
MATCH (d:Personaje)-[:Integrante]->(p:Grupo{nombre:'Siglo Sangriento'}) 
RETURN d.nombre as Personaje, p.nombre as integrante

#8.¿Quiénes pelearon durante el Siglo Sangriento?
MATCH (p)-[:combatio_en]->(e:guerra {nombre: "Siglo Sangriento"}) RETURN p.nombre

#9.Mostrar los personajes que participaron en la Conquista de los Siete Reinos y de que dragón eran jinetes
MATCH (p:Personaje)-[:combatio_en]->(e:guerra {nombre: "Guerra de la Conquista"})
OPTIONAL MATCH (p)-[:Jinete]->(d:Dragon)
RETURN p.nombre AS Nombre, 
       COLLECT(d.nombre) AS Dragones
#10. Mostrar las casas que participaron en la Conquista de los Siete Reinos
MATCH (p:casa)-[:combatio_en]->(e:guerra {nombre: "Guerra de la Conquista"})
RETURN p.nombre AS Nombre;

#11. Mostrar las batallas de la Guerra de la Conquista, donde tuvieron lugar, cuando, quien combatió, quien murió y quien resulto victorioso:
MATCH (b)-[:durante]->(e:guerra {nombre: "Guerra de la Conquista"})
OPTIONAL MATCH (b)-[:ocurrio_en]->(d)
OPTIONAL MATCH (c)-[:combatio_en]->(b)
OPTIONAL MATCH (v)-[:victorioso]->(b)
OPTIONAL MATCH (m)-[:murio_en]->(b)
RETURN b.nombre AS batalla, d.nombre as lugar,v.nombre as victorioso,m.nombre as murio,b.cuando as cuando
 COLLECT(c.nombre) AS combatio

#12. Mostrar quien combatió durante la guerra, donde, cuando, quien resulto victorioso y quien murió
MATCH (e:guerra {nombre: "Primera Guerra Dorniense"})-[:ocurrio_en]->(l)
OPTIONAL MATCH (c)-[:combatio_en]->(e)
OPTIONAL MATCH (v)-[:victorioso]->(e)
OPTIONAL MATCH (m)-[:murio_en]->(e)
RETURN l.nombre as lugar,v.nombre as victorioso,m.nombre as murio, e.cuando as cuando
 COLLECT(c.nombre) AS combatio

#13.Mostrar las relaciones familiares de Aenys I Targaryen y Maegor Targaryen
MATCH (:Personaje {nombre: "Aenys I Targaryen"})-[:Padre|Esposos|Hermanos]->(familiar) RETURN familiar.nombre

MATCH (:Personaje {nombre: "Maegor Targaryen"})-[:Padre|Esposos|Hermanos]->(familiar) RETURN familiar.nombre

#14.Mostrar quien combatió durante la batalla de sucesión, donde, cuando, quien resulto victorioso y quien murió
MATCH (e:batalla {nombre: "Batalla bajo el Ojo de Dioses"})-[:ocurrio_en]->(l)
OPTIONAL MATCH (c)-[:combatio_en]->(e)
OPTIONAL MATCH (v)-[:victorioso]->(e)
OPTIONAL MATCH (m)-[:murio_en]->(e)
RETURN l.nombre as lugar,v.nombre as victorioso,m.nombre as murio,e.cuando as cuando,
 COLLECT(c.nombre) AS combatio

#15.IV.Muestra las relaciones familiares de Jaehaerys I Targaryen
MATCH (:Personaje {nombre: "Jaehaerys I Targaryen"})-[:Padre]->(f)  
OPTIONAL MATCH (f)-[:Jinete]->(d)  
RETURN f.nombre as nombre,f.apodo as apodo,f.nacimiento as nacimiento, f.muerte as muerte,f.titulos as titulos, f.ojos as ojos, f.cabello as cabello, f.genero as genero,  d.nombre as dragon     

#16. V.	Mostrar las batallas ocurridas durante la Danza de Dragones
MATCH (b)-[:durante]->(e:guerra {nombre: "Danza de Dragones"})
OPTIONAL MATCH (b)-[:ocurrio_en]->(d)
OPTIONAL MATCH (c)-[:combatio_en]->(b)
OPTIONAL MATCH (v)-[:victorioso]->(b)
OPTIONAL MATCH (m)-[:murio_en]->(b)
RETURN b.nombre AS batalla, d.nombre as lugar,v.nombre as victorioso,m.nombre as murio,b.cuando as cuando,
 COLLECT(c.nombre) as combatio
 
 #17. Mostrar los integrantes del grupo los Verdes y sus dragones
MATCH (p)-[:Integrante]->(:Grupo {nombre: "los Verdes"}) 
OPTIONAL MATCH (p)-[:Jinete]->(d:Dragon) 
RETURN p.nombre as nombre, p.nacimiento as edad,d.nombre as dragon, d.nacimiento as nacimiento_dragon

#18. Mostrar los integrantes del grupo los Negros
MATCH (p)-[:Integrante]->(:Grupo {nombre: "los Negros"}) 
OPTIONAL MATCH (p)-[:Jinete]->(d:Dragon) 
RETURN p.nombre as nombre, p.nacimiento as edad,d.nombre as dragon, d.nacimiento as nacimiento_dragon

#19.Mostrar quien combatió durante la batalla de sucesión, donde, cuando, quien resulto victorioso y quien murió
MATCH (e:guerra {nombre: "Conquista de Dorne"})-[:ocurrio_en]->(l)
OPTIONAL MATCH (c)-[:combatio_en]->(e)
OPTIONAL MATCH (v)-[:victorioso]->(e)
OPTIONAL MATCH (m)-[:murio_en]->(e)
RETURN e.nombre as guerra,l.nombre as lugar,v.nombre as victorioso,m.nombre as murio, e.cuando as cuando,
collect(c.nombre) as combatio

#20.Mostrar los múltiples hijos de Aegon IV Targaryen
MATCH (e:Personaje{nombre:'Aegon IV Targaryen'} )-[:Padre]->(h) return h.nombre

#21. Mostrar la información sobre la rebelión Blackfyre
MATCH (b)-[:durante]->(e:guerra {nombre: "Rebelión Blackfyre"})
OPTIONAL MATCH (b)-[:ocurrio_en]->(d)
OPTIONAL MATCH (c)-[:combatio_en]->(b)
OPTIONAL MATCH (v)-[:victorioso]->(b)
OPTIONAL MATCH (m)-[:murio_en]->(b)
RETURN b.nombre AS batalla, d.nombre as lugar,v.nombre as victorioso,m.nombre as murio,b.cuando as cuando,
 COLLECT(c.nombre) as combatio
#22. Mostrar los Targaryen muertos durante la Gran Epidemia Primaveral
MATCH (p:Personaje)-[:murio_en]->(a:Acontecimiento{nombre:'Gran Epidemia Primaveral'}) 
RETURN p.nombre as nombre

#23. Mostrar los sucesos de la Rebelión Peake
MATCH (e:guerra {nombre: "Rebelión Peake"})-[:ocurrio_en]->(l)
OPTIONAL MATCH (c)-[:combatio_en]->(e)
OPTIONAL MATCH (v)-[:victorioso]->(e)
OPTIONAL MATCH (m)-[:murio_en]->(e)
RETURN e.nombre as guerra,l.nombre as lugar,v.nombre as victorioso,m.nombre as murio, e.cuando as cuando,
collect(c.nombre) as combatio

#24. Mostrar los sucesos de la Tragedia de Refugio Estival
MATCH (e:Acontecimiento {nombre: "Tragedia de Refugio Estival"})-[:ocurrio_en]->(l)
OPTIONAL MATCH (c)-[:combatio_en]->(e)
OPTIONAL MATCH (v)-[:victorioso]->(e)
OPTIONAL MATCH (m)-[:murio_en]->(e)
RETURN e.nombre as guerra,l.nombre as lugar,v.nombre as victorioso,m.nombre as murio, e.cuando as cuando,
collect(c.nombre) as combatio

#25. Mostrar los sucesos de la guerra
MATCH (e:guerra {nombre: "Guerra de los Reyes Nuevepeniques"})-[:ocurrio_en]->(l)
OPTIONAL MATCH (c)-[:combatio_en]->(e)
OPTIONAL MATCH (v)-[:victorioso]->(e)
OPTIONAL MATCH (m)-[:murio_en]->(e)
RETURN e.nombre as guerra,l.nombre as lugar,v.nombre as victorioso,m.nombre as murio, e.cuando as cuando,
collect(c.nombre) as combatio

#26. Muestra los sucesos ocurridos durante las batallas para destronar a los Targaryen
MATCH (b)-[:durante]->(e:guerra {nombre: "Guerra del Usurpador"})
OPTIONAL MATCH (b)-[:ocurrio_en]->(d)
OPTIONAL MATCH (c)-[:combatio_en]->(b)
OPTIONAL MATCH (v)-[:victorioso]->(b)
OPTIONAL MATCH (m)-[:murio_en]->(b)
RETURN b.nombre AS batalla, d.nombre as lugar,v.nombre as victorioso,m.nombre as murio,b.cuando as cuando,
 COLLECT(c.nombre) as combatio

#27.¿quiénes poseyeron en algún momento las espadas de acero valyrio ahora perdidas Black Sister y Blackfyre? 
MATCH (n:Personaje) 
where n.espada is not null 
RETURN n.nombre as nombre, n.espada as espada

#28. ¿Cuantas parejas de hermanos se casaron entre sí?
MATCH (p1:Personaje)-[Esposos]->(p2:Personaje),
      (p1)-[:Hermanos]->(p2)
RETURN COUNT(p1) AS hermanos_casados

#29.¿Quieres un resumen bélico de Poniente?
Consultar quienes pelearon y ganaron en cada batalla
MATCH (p:Personaje)-[r:combatio_en|victorioso]->(b:batalla)
RETURN b.nombre AS Batalla, COLLECT(DISTINCT p.nombre) AS Participantes, 
       CASE WHEN type(r) = 'victorioso' THEN p.nombre END AS Ganador
       
#30.¿Quienes son los 10 personajes más involucrados en conflictos bélicos?
MATCH (p:Personaje)-[:combatio_en]->(b:batalla)
RETURN p.nombre AS Personaje, COUNT(b) AS num_batallas
ORDER BY num_batallas DESC
LIMIT 10

#31.¿Quieres consultar las relaciones familiares de un personaje en específico? *nota las relaciones de hermanos y esposos se recuperan dos veces porque algunas se definieron como relaciones dirigidas y otras no
MATCH (e:Personaje{nombre:'Daenarys II Targaryen'} )-[]->()
OPTIONAL MATCH (p)-[:Padre]->(e)
OPTIONAL MATCH (e)-[:Padre]->(h)
OPTIONAL MATCH (e)-[:Hermanos]->(he)
OPTIONAL MATCH (e)-[:Hermanos]-(hi)
OPTIONAL MATCH (e)-[:Esposos]->(es)
OPTIONAL MATCH (e)-[:Esposos]-(esi)
RETURN e.nombre as nombre, he.nombre as hermanos, hi.nombre as hermanes, es.nombre as esposos, esi.nombre as esposes,p.nombre as padres, h.nombre as hijos


#32.¿Quieres encontrar todas las batallas que ocurrieron en un lugar en especifico?
MATCH (b:batalla)-[:ocurrio_en]->(l:castillo {nombre: "Harrenhal"})
RETURN b.nombre AS Batalla, b.cuando as cuando

#33.Para enlistar todos los lugares con su respectivo tipo:
MATCH (l)
WHERE l:mar OR l:isla OR l:bahia OR l:region OR l:ciudad OR l:castillo or l:continente
RETURN l.nombre AS Nombre, labels(l) AS Tipo
ORDER BY Tipo, Nombre

#34.¿Quieres saber en donde ocurren eventos y cuándo?
MATCH (l)
WHERE l:mar OR l:isla OR l:bahia OR l:region OR l:ciudad OR l:castillo or l:continente
with l 
MATCH (e)-[:ocurrio_en]->(l) 
RETURN e.nombre AS Evento, l.nombre AS Lugar, e.cuando as cuando

#35.¿Quiere identificar a todos los reyes Targaryen y durante que periodo reinaron?
MATCH (n:Personaje) 
where n.reinado is not null 
RETURN n.nombre as nombre, n.reinado as reinado




















