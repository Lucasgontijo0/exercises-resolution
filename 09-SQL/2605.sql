SELECT
  prod.name,
  prov.name
FROM products prod INNER JOIN providers prov ON prod.id_categories = 6 AND prov.id = prod.id_providers;
