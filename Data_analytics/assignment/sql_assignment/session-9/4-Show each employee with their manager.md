# Show each employee with their manager

SELECT 
    e.name AS employee,
    m.name AS manager
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.id;

-- Show only employees who have no manager

SELECT name AS top_level_manager
FROM employees
WHERE manager_id IS NULL;