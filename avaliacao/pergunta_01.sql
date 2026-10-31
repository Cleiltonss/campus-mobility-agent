SELECT 
    l.endereco,
    COUNT(*) AS chegadas_universidade 
FROM fato_transportes as ft
JOIN dim_local AS l ON l.local_id = ft.destino_id
WHERE l.endereco = 'Av. da Universidade, 1000'
GROUP BY l.endereco