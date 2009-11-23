from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `tasks_task` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `is_active` bool NOT NULL,
        `created_at` datetime NOT NULL,
        `modified_at` datetime NOT NULL,
        `description` longtext NOT NULL,
        `estimate` integer UNSIGNED NOT NULL,
        `completed_at` datetime NULL,
        `user_id` integer NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `tasks_task` ADD CONSTRAINT user_id_refs_id_6ac564e8 FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
"""], sql_down=["""
    DROP TABLE `tasks_task`;
"""])
