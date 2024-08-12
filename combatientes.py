MERGE (start:Personaje {nombre: 'Aegon I Targaryen'})
MERGE (end:guerra {nombre: 'Siglo Sangriento'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:ciudad{nombre: 'Norvos'})                                      
MERGE (end:guerra {nombre: 'Siglo Sangriento'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:ciudad{nombre: 'Qohor'})
MERGE (end:guerra {nombre: 'Siglo Sangriento'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo{nombre: 'Triarquia'})
MERGE (end:guerra {nombre: 'Siglo Sangriento'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo{nombre: 'Triarquia'})
MERGE (end:guerra {nombre: 'Siglo Sangriento'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:ciudad{nombre: 'Volantis'})
MERGE (end:guerra {nombre: 'Siglo Sangriento'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Aegon I Targaryen'})                 
MERGE (end:batalla {nombre: 'Campo de Fuego'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon{nombre: 'Balerion'})
MERGE (end:batalla {nombre: 'Campo de Fuego'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Visenya Targaryen'})
MERGE (end:batalla {nombre: 'Campo de Fuego'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon{nombre: 'Vhagar'})
MERGE (end:batalla {nombre: 'Campo de Fuego'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Rhaenys I Targaryen'})
MERGE (end:batalla {nombre: 'Campo de Fuego'})
MERGE (start)-[:combatio_en]->(end);


MERGE (start:Dragon{nombre: 'Meraxes'})      
MERGE (end:batalla {nombre: 'Campo de Fuego'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Lannister'})
MERGE (end:batalla {nombre: 'Campo de Fuego'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Gardener (extinta)'})
MERGE (end:batalla {nombre: 'Campo de Fuego'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Gardener (extinta)'})
MERGE (end:batalla {nombre: 'Campo de Fuego'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:casa{nombre: 'casa Targaryen'})
MERGE (end:batalla {nombre: 'Campo de Fuego'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:casa {nombre: 'casa Targaryen'})                 
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Targaryen'})                 
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:Personaje {nombre: 'Aegon I Targaryen'})                 
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon{nombre: 'Balerion'})
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Visenya Targaryen'})
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Vhagar'})
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Rhaenys I Targaryen'})
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Meraxes'})
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Lannister'})
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Stark'})
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Hoare (extinta)'})
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Arryn'})
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Gardener (extinta)'})
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Durrandon (extinta)'})
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Martell'})
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Targaryen'})
MERGE (end:guerra {nombre: 'Guerra de la Conquista'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:casa {nombre: 'casa Hoare'})
MERGE (end:batalla {nombre: 'Quema de Harrenhal'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Hoare'})
MERGE (end:batalla {nombre: 'Quema de Harrenhal'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:casa {nombre: 'casa Targaryen'})
MERGE (end:batalla {nombre: 'Quema de Harrenhal'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Tully'})
MERGE (end:batalla {nombre: 'Quema de Harrenhal'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Frey'})
MERGE (end:batalla {nombre: 'Quema de Harrenhal'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Aegon I Targaryen'})
MERGE (end:batalla {nombre: 'Quema de Harrenhal'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Balerion'})
MERGE (end:batalla {nombre: 'Quema de Harrenhal'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Targaryen'})
MERGE (end:batalla {nombre: 'Última Tormenta'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Targaryen'})
MERGE (end:batalla {nombre: 'Última Tormenta'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:Personaje {nombre: 'Rhaenys Targaryen'})
MERGE (end:batalla {nombre: 'Última Tormenta'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Meraxes'})
MERGE (end:batalla {nombre: 'Última Tormenta'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Durrandon (extinta)'})
MERGE (end:batalla {nombre: 'Última Tormenta'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Durrandon (extinta)'})
MERGE (end:batalla {nombre: 'Última Tormenta'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:casa {nombre: 'casa Targaryen'})
MERGE (end:batalla {nombre: 'Quema de Harrenhal'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:Personaje {nombre: 'Rhaenys I Targaryen'})
MERGE (end:guerra {nombre: 'Primera Guerra Dorniense'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Meraxes'})
MERGE (end:guerra {nombre: 'Primera Guerra Dorniense'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Rhaenys I Targaryen'})
MERGE (end:guerra {nombre: 'Primera Guerra Dorniense'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Meraxes'})
MERGE (end:guerra {nombre: 'Primera Guerra Dorniense'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje {nombre: 'Aegon I Targaryen'})
MERGE (end:guerra {nombre: 'Primera Guerra Dorniense'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Balerion'})
MERGE (end:guerra {nombre: 'Primera Guerra Dorniense'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Visenya Targaryen'})
MERGE (end:guerra {nombre: 'Primera Guerra Dorniense'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Vhagar'})
MERGE (end:guerra {nombre: 'Primera Guerra Dorniense'})
MERGE (start)-[:combatio_en]->(end);



MERGE (start:casa {nombre: 'casa Martell'})
MERGE (end:guerra {nombre: 'Primera Guerra Dorniense'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Martell'})
MERGE (end:guerra {nombre: 'Primera Guerra Dorniense'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:casa {nombre: 'casa Baratheon'})
MERGE (end:guerra {nombre: 'Primera Guerra Dorniense'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Hightower'})
MERGE (end:guerra {nombre: 'Primera Guerra Dorniense'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Tyrell'})
MERGE (end:guerra {nombre: 'Primera Guerra Dorniense'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Maegor Targaryen'})
MERGE (end:batalla {nombre: 'Batalla bajo el Ojo de Dioses'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Maegor Targaryen'})
MERGE (end:batalla {nombre: 'Batalla bajo el Ojo de Dioses'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:Dragon {nombre: 'Balerion'})
MERGE (end:batalla {nombre: 'Batalla bajo el Ojo de Dioses'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Aegon Targaryen (el No Coronado)'})
MERGE (end:batalla {nombre: 'Batalla bajo el Ojo de Dioses'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Quicksilver'})
MERGE (end:batalla {nombre: 'Batalla bajo el Ojo de Dioses'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Aegon Targaryen (el No Coronado)'})
MERGE (end:batalla {nombre: 'Batalla bajo el Ojo de Dioses'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Quicksilver'})
MERGE (end:batalla {nombre: 'Batalla bajo el Ojo de Dioses'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje {nombre: 'Aemond Targaryen'})
MERGE (end:batalla {nombre: 'Persecución de la Bahía de los Naufragios'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Vhagar'})
MERGE (end:batalla {nombre: 'Persecución de la Bahía de los Naufragios'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Lucerys Velaryon'})
MERGE (end:batalla {nombre: 'Persecución de la Bahía de los Naufragios'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Arrax'})
MERGE (end:batalla {nombre: 'Persecución de la Bahía de los Naufragios'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Lucerys Velaryon'})
MERGE (end:batalla {nombre: 'Persecución de la Bahía de los Naufragios'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Arrax'})
MERGE (end:batalla {nombre: 'Persecución de la Bahía de los Naufragios'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Grupo {nombre: 'los Verdes'})
MERGE (end:batalla {nombre: 'Persecución de la Bahía de los Naufragios'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Negros'})
MERGE (end:batalla {nombre: 'Persecución de la Bahía de los Naufragios'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Verdes'})
MERGE (end:batalla {nombre: 'Persecución de la Bahía de los Naufragios'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:Dragon {nombre: 'Syrax'})
MERGE (end:Acontecimiento {nombre: 'Asalto a Pozo Dragón'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Dreamfyre'})
MERGE (end:Acontecimiento {nombre: 'Asalto a Pozo Dragón'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Tiraxes'})
MERGE (end:Acontecimiento {nombre: 'Asalto a Pozo Dragón'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Morghul'})
MERGE (end:Acontecimiento {nombre: 'Asalto a Pozo Dragón'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Shrykos'})
MERGE (end:Acontecimiento {nombre: 'Asalto a Pozo Dragón'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje {nombre: 'Joffrey Velaryon'})
MERGE (end:Acontecimiento {nombre: 'Asalto a Pozo Dragón'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje {nombre: 'Daemon Targaryen'})
MERGE (end:guerra {nombre: 'Guerra de los Peldaños de Piedra'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Meraxes'})
MERGE (end:guerra{nombre: 'Guerra de los Peldaños de Piedra'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Corlys Velaryon'})
MERGE (end:guerra {nombre: 'Guerra de los Peldaños de Piedra'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa {nombre: 'casa Martell'})
MERGE (end:guerra {nombre: 'Guerra de los Peldaños de Piedra'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'Triarquia'})
MERGE (end:guerra {nombre: 'Guerra de los Peldaños de Piedra'})
MERGE (start)-[:combatio_en]->(end);

MERGE(start:casa {nombre: 'casa Martell'})
MERGE (end:guerra {nombre: 'Guerra de los Peldaños de Piedra'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:Grupo {nombre: 'Triarquia'})
MERGE (end:guerra {nombre: 'Guerra de los Peldaños de Piedra'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:Personaje {nombre: 'Daemon Targaryen'})
MERGE (end:batalla {nombre: 'Batalla sobre el Ojo de Dioses'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Caraxes'})
MERGE (end:batalla {nombre: 'Batalla sobre el Ojo de Dioses'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Aemond Targaryen'})
MERGE (end:batalla {nombre: 'Batalla sobre el Ojo de Dioses'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Vhagar'})
MERGE (end:batalla {nombre: 'Batalla sobre el Ojo de Dioses'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Daemon Targaryen'})
MERGE (end:batalla {nombre: 'Batalla sobre el Ojo de Dioses'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Caraxes'})
MERGE (end:batalla {nombre: 'Batalla sobre el Ojo de Dioses'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje {nombre: 'Aemond Targaryen'})
MERGE (end:batalla {nombre: 'Batalla sobre el Ojo de Dioses'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Vhagar'})
MERGE (end:batalla {nombre: 'Batalla sobre el Ojo de Dioses'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Grupo {nombre: 'los Verdes'})
MERGE (end:batalla {nombre: 'Batalla sobre el Ojo de Dioses'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Negros'})
MERGE (end:batalla {nombre: 'Batalla sobre el Ojo de Dioses'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Verdes'})
MERGE (end:batalla {nombre: 'Batalla de Reposo del Grajo'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Negros'})
MERGE (end:batalla {nombre: 'Batalla de Reposo del Grajo'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Verdes'})
MERGE (end:batalla {nombre: 'Batalla de Reposo del Grajo'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:Personaje {nombre: 'Criston Cole'})
MERGE (end:batalla {nombre: 'Batalla de Reposo del Grajo'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Aegon II Targaryen'})
MERGE (end:batalla {nombre: 'Batalla de Reposo del Grajo'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Sunfyre'})
MERGE (end:batalla {nombre: 'Batalla de Reposo del Grajo'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Aemond Targaryen'})
MERGE (end:batalla {nombre: 'Batalla de Reposo del Grajo'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Vhagar'})
MERGE (end:batalla {nombre: 'Batalla de Reposo del Grajo'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Rhaenys II Targaryen'})
MERGE (end:batalla {nombre: 'Batalla de Reposo del Grajo'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Meleys'})
MERGE (end:batalla {nombre: 'Batalla de Reposo del Grajo'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Rhaenys II Targaryen'})
MERGE (end:batalla {nombre: 'Batalla de Reposo del Grajo'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Meleys'})
MERGE (end:batalla {nombre: 'Batalla de Reposo del Grajo'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje {nombre: 'Jaehaerys Targaryen'})
MERGE (end:Acontecimiento {nombre: 'Sangre y Queso'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Grupo {nombre: 'los Verdes'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Negros'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'Triarquia'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Jacaerys Velaryon'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Vermax'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Corlys Velaryon'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Jacaerys Velaryon'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Vermax'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje {nombre: 'Aegon III Targaryen'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Stormcloud'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Stormcloud'})
MERGE (end:batalla{nombre: 'Batalla del Gaznate'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje {nombre: 'Ulf el Blanco'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Silverwing'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Nettles'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Sheepstealer'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Addam Velaryon'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Seasmoke'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Hugh Hammer'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Vermithor'})
MERGE (end:batalla {nombre: 'Batalla del Gaznate'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Verdes'})
MERGE (end:batalla {nombre: 'Batalla del Aguamiel'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Verdes'})
MERGE (end:batalla {nombre: 'Batalla del Aguamiel'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:Grupo {nombre: 'los Negros'})
MERGE (end:batalla {nombre: 'Batalla del Aguamiel'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Daeron Targaryen'})
MERGE (end:batalla {nombre: 'Batalla del Aguamiel'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Tessarion'})
MERGE (end:batalla {nombre: 'Batalla del Aguamiel'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Negros'})
MERGE (end:batalla {nombre: 'Conquista de la Capital'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Negros'})
MERGE (end:batalla {nombre: 'Conquista de la Capital'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:Grupo {nombre: 'los Verdes'})
MERGE (end:batalla {nombre: 'Conquista de la Capital'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Negros'})
MERGE (end:batalla {nombre: 'Conquista de la Capital'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:Personaje {nombre: 'Daemon Targaryen'})
MERGE (end:batalla {nombre: 'Conquista de la Capital'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Corlys Velaryon'})
MERGE (end:batalla {nombre: 'Conquista de la Capital'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Alicent Hightower'})
MERGE (end:batalla {nombre: 'Conquista de la Capital'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Otto Hightower'})
MERGE (end:batalla {nombre: 'Conquista de la Capital'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Otto Hightower'})
MERGE (end:batalla {nombre: 'Conquista de la Capital'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje {nombre: 'Gwayne Hightower'})
MERGE (end:batalla {nombre: 'Conquista de la Capital'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Gwayne Hightower'})
MERGE (end:batalla {nombre: 'Conquista de la Capital'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Syrax'})
MERGE (end:batalla {nombre: 'Conquista de la Capital'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Caraxes'})
MERGE (end:batalla {nombre: 'Conquista de la Capital'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Rhaenyra Targaryen'})
MERGE (end:batalla {nombre: 'Conquista de la Capital'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Verdes'})
MERGE (end:batalla {nombre: 'Caída de Rocadragón'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Verdes'})
MERGE (end:batalla {nombre: 'Caída de Rocadragón'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:Grupo {nombre: 'los Negros'})
MERGE (end:batalla {nombre: 'Caída de Rocadragón'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Aegon II Targaryen'})
MERGE (end:batalla {nombre: 'Caída de Rocadragón'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Baela Targaryen'})
MERGE (end:batalla {nombre: 'Caída de Rocadragón'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Sunfyre'})
MERGE (end:batalla {nombre: 'Caída de Rocadragón'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Moondancer'})
MERGE (end:batalla {nombre: 'Caída de Rocadragón'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Moondancer'})
MERGE (end:batalla {nombre: 'Caída de Rocadragón'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Vermithor'})
MERGE (end:batalla {nombre: 'Batalla de Ladera'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Silverwing'})
MERGE (end:batalla {nombre: 'Batalla de Ladera'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Hugh Hammer'})
MERGE (end:batalla {nombre: 'Batalla de Ladera'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Ulf el Blanco'})
MERGE (end:batalla {nombre: 'Batalla de Ladera'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Verdes'})
MERGE (end:batalla {nombre: 'Batalla de Ladera'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Negros'})
MERGE (end:batalla {nombre: 'Batalla de Ladera'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Verdes'})
MERGE (end:batalla {nombre: 'Batalla de Ladera'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:Grupo {nombre: 'los Verdes'})
MERGE (end:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Grupo {nombre: 'los Negros'})
MERGE (end:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Addam Velaryon'})
MERGE (end:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Addam Velaryon'})
MERGE (end:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje {nombre: 'Daeron Targaryen'})
MERGE (end:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Daeron Targaryen'})
MERGE (end:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje {nombre: 'Hugh Hammer'})
MERGE (end:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje {nombre: 'Hugh Hammer'})
MERGE (end:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Seasmoke'})
MERGE (end:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Seasmoke'})
MERGE (end:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Vermithor'})
MERGE (end:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Vermithor'})
MERGE (end:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Tessarion'})
MERGE (end:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Dragon {nombre: 'Tessarion'})
MERGE (end:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Dragon {nombre: 'Silverwing'})
MERGE (end:batalla {nombre: 'Segunda Batalla de Ladera'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Daeron II Targaryen'})
MERGE (end:Acontecimiento {nombre: 'Gran Epidemia Primaveral'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje{nombre: 'Valarr Targaryen'})
MERGE (end:Acontecimiento {nombre: 'Gran Epidemia Primaveral'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje{nombre: 'Matarys Targaryen'})
MERGE (end:Acontecimiento {nombre: 'Gran Epidemia Primaveral'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje{nombre: 'Aegon V Targaryen'})
MERGE (end:Acontecimiento {nombre: 'Tragedia de Refugio Estival'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje{nombre: 'Duncan Targaryen'})
MERGE (end:Acontecimiento {nombre: 'Tragedia de Refugio Estival'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje{nombre: 'Daemon I Blackfyre'})
MERGE (end:batalla {nombre: 'Batalla del Padro Hierbarroja'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje{nombre: 'Daemon I Blackfyre'})
MERGE (end:batalla {nombre: 'Batalla del Padro Hierbarroja'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Maekar I Targaryen'})
MERGE (end:batalla {nombre: 'Batalla del Padro Hierbarroja'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Baelor Targaryen'})
MERGE (end:batalla {nombre: 'Batalla del Padro Hierbarroja'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Targaryen'})
MERGE (end:guerra {nombre: 'Batalla del Prado Hierbarroja'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Blackfyre'})
MERGE (end:guerra {nombre: 'Batalla del Prado Hierbarroja'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Targaryen'})
MERGE (end:guerra {nombre: 'Batalla del Prado Hierbarroja'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:Personaje{nombre: 'Maekar I Targaryen'})
MERGE (end:guerra {nombre: 'Rebelión Peake'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Maekar I Targaryen'})
MERGE (end:guerra {nombre: 'Rebelión Peake'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:casa{nombre: 'casa Targaryen'})
MERGE (end:guerra {nombre: 'Rebelión Peake'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Peake'})
MERGE (end:guerra {nombre: 'Rebelión Peake'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Targaryen'})
MERGE (end:guerra {nombre: 'Rebelión Peake'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:casa{nombre: 'casa Targaryen'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Tyrell'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Martell'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Baratheon'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Baratheon'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:casa{nombre: 'casa Stark'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Arryn'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Tully'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Lannister'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Greyjoy'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Aerys II Targaryen'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Rhaegar Targaryen'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Robert Baratheon'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Stannis Baratheon'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Eddard Stark'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Tywin Lannister'})
MERGE (end:guerra {nombre: 'Guerra del Usurpador'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Rhaegar Targaryen'})
MERGE (end:batalla {nombre: 'Batalla del Tridente'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Rhaegar Targaryen'})
MERGE (end:batalla {nombre: 'Batalla del Tridente'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje{nombre: 'Robert Baratheon'})
MERGE (end:batalla {nombre: 'Batalla del Tridente'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Baratheon'})
MERGE (end:batalla {nombre: 'Batalla del Tridente'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Eddard Stark'})
MERGE (end:batalla {nombre: 'Batalla del Tridente'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Aerys II Targaryen'})
MERGE (end:batalla {nombre: 'Saqueo de Desembarco del Rey'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Aerys II Targaryen'})
MERGE (end:batalla {nombre: 'Saqueo de Desembarco del Rey'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:casa{nombre: 'casa Lannister'})
MERGE (end:batalla {nombre: 'Saqueo de Desembarco del Rey'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Jaime Lannister'})
MERGE (end:batalla {nombre: 'Saqueo de Desembarco del Rey'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Tywin Lannister'})
MERGE (end:batalla {nombre: 'Saqueo de Desembarco del Rey'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Elia Martell'})
MERGE (end:batalla {nombre: 'Saqueo de Desembarco del Rey'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje{nombre: 'Rhaenys III Targaryen'})
MERGE (end:batalla {nombre: 'Saqueo de Desembarco del Rey'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje{nombre: 'Daeron I Targaryen'})
MERGE (end:guerra {nombre: 'Conquista de Dorne'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:Personaje{nombre: 'Daeron I Targaryen'})
MERGE (end:guerra {nombre: 'Conquista de Dorne'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Targaryen'})
MERGE (end:guerra {nombre: 'Conquista de Dorne'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Velaryon'})
MERGE (end:guerra {nombre: 'Conquista de Dorne'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Tyrell'})
MERGE (end:guerra {nombre: 'Conquista de Dorne'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Stark'})
MERGE (end:guerra {nombre: 'Conquista de Dorne'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Martell'})
MERGE (end:guerra {nombre: 'Conquista de Dorne'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Martell'})
MERGE (end:guerra {nombre: 'Conquista de Dorne'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:casa{nombre: 'casa Targaryen'})
MERGE (end:guerra {nombre: 'Guerra de los Reyes Nuevepeniques'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Targaryen'})
MERGE (end:guerra {nombre: 'Guerra de los Reyes Nuevepeniques'})
MERGE (start)-[:victorioso]->(end);

MERGE (start:casa{nombre: 'casa Blackfyre'})
MERGE (end:guerra {nombre: 'Guerra de los Reyes Nuevepeniques'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Blackfyre'})
MERGE (end:guerra {nombre: 'Guerra de los Reyes Nuevepeniques'})
MERGE (start)-[:murio_en]->(end);

MERGE (start:casa{nombre: 'casa Baratheon'})
MERGE (end:guerra {nombre: 'Guerra de los Reyes Nuevepeniques'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Greyjoy'})
MERGE (end:guerra {nombre: 'Guerra de los Reyes Nuevepeniques'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:casa{nombre: 'casa Hightower'})
MERGE (end:guerra {nombre: 'Guerra de los Reyes Nuevepeniques'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Jaehaerys II Targaryen'})
MERGE (end:guerra {nombre: 'Guerra de los Reyes Nuevepeniques'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Barristan Selmy'})
MERGE (end:guerra {nombre: 'Guerra de los Reyes Nuevepeniques'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Aerys II Targaryen'})
MERGE (end:guerra {nombre: 'Guerra de los Reyes Nuevepeniques'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Maelys I Blackfyre'})
MERGE (end:guerra {nombre: 'Guerra de los Reyes Nuevepeniques'})
MERGE (start)-[:combatio_en]->(end);

MERGE (start:Personaje{nombre: 'Maelys I Blackfyre'})
MERGE (end:guerra {nombre: 'Guerra de los Reyes Nuevepeniques'})
MERGE (start)-[:murio_en]->(end);





































































