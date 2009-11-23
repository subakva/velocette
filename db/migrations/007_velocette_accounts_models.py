from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `accounts_profile` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `is_active` bool NOT NULL,
        `created_at` datetime NOT NULL,
        `modified_at` datetime NOT NULL,
        `user_id` integer NOT NULL UNIQUE,
        `time_zone` varchar(100) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `accounts_profile` ADD CONSTRAINT user_id_refs_id_46e869e2 FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
"""], sql_down=["""
    DROP TABLE `accounts_profile`;
"""])
