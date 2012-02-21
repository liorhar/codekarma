drop table if exists commits;
create table commits (
  id integer primary key autoincrement,
  author string not null,
  message string not null,
  score integer not null,
  time timestamp not null
);
