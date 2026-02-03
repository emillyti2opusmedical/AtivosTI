INSERT INTO updates (script, applied_at)VALUES (
    'ALTER TABLE ativos ADD COLUMN localizacao TEXT;',
    CURRENT_TIMESTAP
);