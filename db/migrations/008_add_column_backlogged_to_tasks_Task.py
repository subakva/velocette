from dmigrations.mysql import migrations as m
import datetime
migration = m.AddColumn('tasks', 'Task', 'backlogged', 'bool NOT NULL')
