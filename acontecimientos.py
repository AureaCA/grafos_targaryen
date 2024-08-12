MERGE (n:Acontecimiento {nombre: 'La Perdición de Valyria',cuando:'102 ac',
                         descripcion:'Cataclismo de naturaleza no especificada que
causó el colapso del territorio valiriano, que comprendía mucho del territorio
de Essos, que había prosperado durante cinco mil años. '});

MERGE (start:Acontecimiento {nombre: 'La Perdición de Valyria'})
MERGE (end:ciudad {nombre: 'Valyria'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (n:guerra {nombre: 'Siglo Sangriento',cuando:'102 ac-2bc',
                         descripcion:'fue un período de caos en Essos que duró aproximadamente un siglo y comenzó tras la Maldición de Valyria. Este período está marcado por guerras entre las Ciudades Libres y por la hegemonía y posterior caída de Volantis. '});

MERGE (start:guerra {nombre: 'Siglo Sangriento'})
MERGE (end:region {nombre: 'Feudo Franco de Valyria'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:guerra {nombre: 'Siglo Sangriento'})
MERGE (end:region {nombre: 'Ciudades Libres'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (n:guerra {nombre: 'Guerra de la Conquista',cuando:'2 ac-1 dc',
                         descripcion:' fue la campaña militar liderada por Aegon Targaryen para conquistar las tierras de Poniente al sur del Muro. Entre sus fuerzas se contaban los soldados de Rocadragón y sus vasallos, sus hermanas Visenya y Rhaenys y sus tres dragones, Balerion, Vhagar y Meraxes, además de algunas casas que se rebelaron a sus señores, se rindieron voluntariamente o cambiaron de bando al ser conquistadas. Ocurrió entre los años 2 A.C hasta el 1 D.C. Resultados: 
Aegon I Targaryen conquista seis de los Siete Reinos, creación del Trono de Hierro, Dorne se mantiene independiente'});

MERGE (start:guerra {nombre: 'Guerra de la Conquista'})
MERGE (end:continente {nombre: 'Poniente'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (n:batalla {nombre: 'Campo de Fuego',cuando:'2 ac',
                         descripcion:'fue una importante batalla durante la Guerra de la Conquista. De acuerdo a fuentes semi canónicas, la batalla tuvo lugar en la región norte del Dominio en el 2 A.C. Los Conquistadores de la casa Targaryen se enfrento con 11mil hombres y 3 dragones contra las fuerzas del Dominio y Roca Casterly que conformaban un ejercito de 55mil hombres. Hacia el final del Siglo de Sangre, Pentos y Tyrosh se acercaron al joven Lord Aegon Targaryen, jinete del dragón Balerion, para formar una alianza. Aegon, montado en su dragón Balerion, voló para encontrarse con el Príncipe de Pentos y luego a Lys, donde prendió fuego a la flota volantena. Con la campaña de Volantis terminada, regresó a Rocadragón y centró su atención en las tierras del oeste, que siempre habían sido de su interés.'});

MERGE (start:batalla {nombre: 'Campo de Fuego'})
MERGE (end:region{nombre: 'el Dominio'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:batalla {nombre: 'Campo de Fuego'})
MERGE (end:guerra{nombre: 'Guerra de la Conquista'})
MERGE (start)-[:durante]->(end);



MERGE (n:batalla {nombre:'Quema de Harrenhal',cuando:'2 ac',
                         descripcion:'fue una batalla acaecida durante la Guerra de la Conquista. Aegon el Conquistador a lomos de su dragón, Balerion, provocó la quema de la fortaleza de Harrenhal, muriendo el rey Harren el Negro y terminando con su linaje'});

MERGE (start:batalla {nombre: 'Quema de Harrenhal'})
MERGE (end:castillo {nombre: 'Harrenhal'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:batalla {nombre: 'Quema de Harrenhal'})
MERGE (end:guerra{nombre: 'Guerra de la Conquista'})
MERGE (start)-[:durante]->(end);

MERGE (n:batalla {nombre:'Última Tormenta',cuando:'2 ac-1 dc',
                         descripcion:'fue una de las principales batallas acaecidas durante la Guerra de la Conquista. Resultó en la caída del Reino de las Tierras de la Tormenta y en la fundación de la Casa Baratheon'});

MERGE (start:batalla {nombre: 'Última Tormenta'})
MERGE (end:castillo {nombre: 'Bastión de Tormentas'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:batalla {nombre: 'Última Tormenta'})
MERGE (end:guerra{nombre: 'Guerra de la Conquista'})
MERGE (start)-[:durante]->(end);

MERGE (n:Acontecimiento {nombre: 'Coronación de Aegón I',cuando:'1 dc',
                         descripcion:'año 1 la coronación de Aegon como Rey de los Siete Reinos en Antigua. En el lugar de su llegada al continente, Aegon funda Desembarco del Rey, que se convertirá en la capital de la dinastía Targaryen durante casi 300 años'});

MERGE (start:Acontecimiento {nombre: 'Coronación de Aegon I'})
MERGE (end:ciudad {nombre: 'Antigua'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (n:guerra {nombre: 'Primera Guerra Dorniense',cuando:'4-13 dc'});

MERGE (start:guerra {nombre: 'Primera Guerra Dorniense'})
MERGE (end:region {nombre: 'Dorne'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (n:batalla {nombre: 'Batalla bajo el Ojo de Dioses',cuando:'43 dc'});

MERGE (start:batalla {nombre: 'Batalla bajo el Ojo de Dioses'})
MERGE (end:region {nombre: 'Tierras de los Ríos'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (n:guerra {nombre: 'Danza de Dragones',cuando:'129-131 dc'});

MERGE (start:guerra {nombre: 'Danza de Dragones'})
MERGE (end:continente {nombre: 'Poniente'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (n:batalla {nombre:'Persecución de la Bahía de los Naufragios',cuando:'129 dc',
                         descripcion:'Al comienzo de la guerra <<La Danza de los Dragones>>, Lucerys Velaryon fue enviado a Bastión de Tormentas para forjar una alianza con Lord Borros Baratheon.  Se dirigió al castillo montado en su dragón y allí se encontró con su tío Aemond Targaryen, el cual también había sido enviado a negociar una alianza. Lord Borros Baratheon rechazó la propuesta de los Negros y aceptó la propuesta de los Verdes, pero se negó a asesinar a Lucerys como pedía este último. Lucerys se marchó de vuelta a Rocadragón sobre Arrax en medio de una gran tormenta. En el camino, fue perseguido por Aemond y su dragón Vhagar. La cabeza y cuello del dragón Arrax fueron enviados a tierra por el mar debajo de los acantilados cercanos a Bastión de Tormentas tres días después. El cadáver del príncipe Lucerys nunca apareció. Con la muerte de Luke, la Danza de los Dragones dejó de ser una cuestión de diplomacia y comenzó una guerra de fuego y sangre', ocurrio_en:'129 dc en la Bahía de los Naufragios'});

MERGE (start:batalla {nombre: 'Persecución de la Bahía de los Naufragios'})
MERGE (end:bahia {nombre: 'Bahía de los Naufragios'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:batalla {nombre: 'Persecución de la Bahía de los Naufragios'})
MERGE (end:guerra{nombre: 'Danza de Dragones'})
MERGE (start)-[:durante]->(end);

MERGE (n:Acontecimiento {nombre:'Asalto a Pozo Dragón',cuando:'130 ac',descripcion:'tuvo lugar durante el motín del Desembarco del Rey durante la Danza de los Dragones. Durante los disturbios, una turba loca, forzó su entrada en Pozo Dragón en la colina de Rhaenys y mataron a los cuatro dragones alojados, así como al dragón Syrax, que fue soltado por el principe Joffrey Velaryon y volaba por encima de la ciudad.

Los cuatro dragones estaban alojados en su interior eran: Shrykos, sin reclamar desde la muerte del príncipe Jaehaerys Targaryen; Morghul, el dragón de la princesa Jaehaera Targaryen ; Tiraxes, el dragón montado por el príncipe Joffrey Velaryon; y Dreamfyre, no reclamado desde la muerte de la reina Helaena Targaryen.', ocurrio_en:'130 dc en Desembarco del Rey'});

MERGE (start:Acontecimiento {nombre: 'Asalto a Pozo Dragón'})
MERGE (end:ciudad {nombre: 'Desembarco del Rey'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:Acontecimiento {nombre: 'Asalto a Pozo Dragón'})
MERGE (end:guerra{nombre: 'Danza de Dragones'})
MERGE (start)-[:durante]->(end);

MERGE (n:guerra {nombre: 'Guerra de los Peldaños de Piedra',cuando:'106-115 dc'});

MERGE (start:guerra {nombre: 'Guerra de los Peldaños de Piedra'})
MERGE (end:mar {nombre: 'Mar Angosto'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (n:batalla {nombre: 'Batalla sobre el Ojo de Dioses',cuando:'130 dc'});

MERGE (start:batalla {nombre: 'Batalla sobre el Ojo de Dioses'})
MERGE (end:castillo {nombre: 'Harrenhal'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:batalla {nombre: 'Batalla sobre el Ojo de Dioses'})
MERGE (end:guerra{nombre: 'Danza de Dragones'})
MERGE (start)-[:durante]->(end);

MERGE (n:batalla{nombre: 'Batalla de Reposo del Grajo',cuando:'129 dc'});

MERGE (start:batalla{nombre: 'Batalla de Reposo del Grajo'})
MERGE (end:region {nombre: 'Tierras de la Corona'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:batalla {nombre: 'Batalla sobre el Ojo de Dioses'})
MERGE (end:guerra{nombre: 'Danza de Dragones'})
MERGE (start)-[:durante]->(end);

MERGE (n:Acontecimiento {nombre: 'Sangre y Queso',cuando:'129 dc'});

MERGE (start:Acontecimiento {nombre: 'Sangre y Queso'})
MERGE (end:castillo {nombre: 'Desembarco del Rey'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:Acontecimiento {nombre: 'Batalla sobre el Ojo de Dioses'})
MERGE (end:guerra{nombre: 'Danza de Dragones'})
MERGE (start)-[:durante]->(end);

MERGE (n:batalla {nombre: 'Batalla del Gaznate',cuando:'130 dc'});

MERGE (start:batalla {nombre: 'Batalla del Gaznate'})
MERGE (end:bahia {nombre: 'Bahía del Aguasnegras'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:batalla {nombre: 'Batalla del Gaznate'})
MERGE (end:guerra{nombre: 'Danza de Dragones'})
MERGE (start)-[:durante]->(end);

MERGE (n:batalla {nombre: 'Batalla del Aguamiel',cuando:'130 dc'});

MERGE (start:batalla {nombre: 'Batalla del Aguamiel'})
MERGE (end:region {nombre: 'el Dominio'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:batalla {nombre: 'Batalla del Aguamiel'})
MERGE (end:guerra{nombre: 'Danza de Dragones'})
MERGE (start)-[:durante]->(end);

MERGE (n:batalla {nombre: 'Conquista de la Capital',cuando:'130 dc'});

MERGE (start:batalla {nombre: 'Conquista de la Capital'})
MERGE (end:ciudad {nombre: 'Desembarco del Rey'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:batalla {nombre: 'Conquista de la Capital'})
MERGE (end:guerra{nombre: 'Danza de Dragones'})
MERGE (start)-[:durante]->(end);

MERGE (n:batalla {nombre: 'Caída de Rocadragón',cuando:'130 dc'});

MERGE (start:batalla {nombre: 'Conquista de la Capital'})
MERGE (end:isla {nombre: 'Rocadragón'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:batalla {nombre: 'Caída de Rocadragón'})
MERGE (end:guerra{nombre: 'Danza de Dragones'})
MERGE (start)-[:durante]->(end);

MERGE (n:batalla {nombre: 'Batalla de Ladera',cuando:'130 dc'});

MERGE (start:batalla {nombre: 'Batalla de Ladera'})
MERGE (end:region {nombre: 'el Dominio'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:batalla {nombre: 'Batalla de Ladera'})
MERGE (end:guerra{nombre: 'Danza de Dragones'})
MERGE (start)-[:durante]->(end);

MERGE (n:batalla {nombre: 'Segunda Batalla de Ladera',cuando:'130 dc'});

MERGE (start:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (end:region {nombre: 'el Dominio'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (end:guerra{nombre: 'Danza de Dragones'})
MERGE (start)-[:durante]->(end);



MERGE (n:Acontecimiento {nombre: 'Gran Epidemia Primaveral',cuando:'209-210 dc'});

MERGE (start:Acontecimiento {nombre: 'Gran Epidemia Primaveral'})
MERGE (end:continente {nombre: 'Poniente'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (n:Acontecimiento {nombre: 'Tragedia de Refugio Estival',cuando:'259 dc'});

MERGE (start:Acontecimiento {nombre: 'Tragedia de Refugio Estival'})
MERGE (end:region {nombre: 'Dorne'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (n:guerra {nombre: 'Rebelión Blackfyre',cuando:'196 dc'});

MERGE (start:guerra {nombre: 'Rebelión Blackfyre'})
MERGE (end:region {nombre: 'Tierras de los Ríos'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:guerra {nombre: 'Rebelión Blackfyre'})
MERGE (end:region {nombre: 'Tierras del Oeste'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:guerra {nombre: 'Rebelión Blackfyre'})
MERGE (end:region {nombre: 'el Dominio'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (n:batalla {nombre: 'Batalla del Padro Hierbarroja',cuando:'196 dc'});

MERGE (start:batalla {nombre: 'Batalla del Padro Hierbarroja'})
MERGE (end:guerra {nombre: 'Rebelión Blackfyre'})
MERGE (start)-[:durante]->(end);

MERGE (n:guerra {nombre: 'Rebelión Peake',cuando:'233 dc'});

MERGE (start:guerra {nombre: 'Rebelión Peake'})
MERGE (end:region {nombre: 'el Dominio'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (n:guerra {nombre: 'Guerra de los Reyes Nuevepeniques',cuando:'260 dc'});

MERGE (start:guerra {nombre: 'Guerra de los Reyes Nuevepeniques'})
MERGE (end:mar {nombre: 'Mar Angosto'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (n:guerra {nombre: 'Guerra del Usurpador',cuando:'282-283 dc'});

MERGE (start:guerra {nombre: 'Guerra del Usurpador'})
MERGE (end:continente {nombre: 'Poniente'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (n:batalla {nombre: 'Batalla del Tridente',cuando:'283 dc'});

MERGE (start:batalla {nombre: 'Batalla del Tridente'})
MERGE (end:region {nombre: 'Tierras de los Ríos'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:batalla {nombre: 'Batalla del Tridente'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:durante]->(end);

MERGE (start:batalla {nombre: 'Saqueo de Desembarco del Rey',cuando:'283 dc'})
MERGE (end:ciudad {nombre: 'Desembarco del Rey'})
MERGE (start)-[:ocurrio_en]->(end);

MERGE (start:batalla {nombre: 'Saqueo de Desembarco del Rey'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:durante]->(end);

MERGE (start:guerra {nombre: 'Conquista de Dorne',cuando:'157-161 dc'})
MERGE (end:region {nombre: 'Dorne'})
MERGE (start)-[:ocurrio_en]->(end);


