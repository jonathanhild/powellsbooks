# Powells Books Database Schema

Document created on: 2020-10-22 12:21:33.054158

Database path: /home/jonathan/Source/powellsbooks/./db/powells.db

## BOOK

| ID | Name | Type | Not Null | Default Value | Primary Key |
| --- | --- | --- | --- | --- | --- |
| 0 | id | INTEGER | No | None | Yes |
| 1 | title | TEXT | Yes | None | No |
| 2 | isbn13 | TEXT | Yes | None | No |
| 3 | publisher | TEXT | Yes | None | No |
| 4 | publication_date | TEXT | No | None | No |
| 5 | series | TEXT | No | None | No |
| 6 | series_num | INTEGER | No | None | No |
| 7 | pages | INTEGER | No | None | No |
| 8 | avg_customer_rating | REAL | No | None | No |
| 9 | customer_ratings | INTEGER | No | None | No |
| 10 | publisher_comment | TEXT | No | None | No |
## SQLITE_SEQUENCE

| ID | Name | Type | Not Null | Default Value | Primary Key |
| --- | --- | --- | --- | --- | --- |
| 0 | name |  | No | None | No |
| 1 | seq |  | No | None | No |
## AUTHOR

| ID | Name | Type | Not Null | Default Value | Primary Key |
| --- | --- | --- | --- | --- | --- |
| 0 | id | INTEGER | No | None | Yes |
| 1 | author_name | TEXT | Yes | None | No |
## AUTHOR_BOOK

| ID | Name | Type | Not Null | Default Value | Primary Key |
| --- | --- | --- | --- | --- | --- |
| 0 | author_id | INTEGER | Yes | None | No |
| 1 | book_id | INTEGER | Yes | None | No |
## SYNOPSIS_REVIEW

| ID | Name | Type | Not Null | Default Value | Primary Key |
| --- | --- | --- | --- | --- | --- |
| 0 | id | INTEGER | No | None | Yes |
| 1 | book_id | INTEGER | Yes | None | No |
| 2 | synopsis_type | TEXT | Yes | None | No |
| 3 | synopsis_blurb | TEXT | Yes | None | No |
| 4 | synopsis_source | TEXT | Yes | None | No |
## READER_REVIEW

| ID | Name | Type | Not Null | Default Value | Primary Key |
| --- | --- | --- | --- | --- | --- |
| 0 | id | INTEGER | No | None | Yes |
| 1 | book_id | INTEGER | Yes | None | No |
| 2 | rating | INTEGER | Yes | None | No |
| 3 | review_blurb | TEXT | Yes | None | No |
## STAFF

| ID | Name | Type | Not Null | Default Value | Primary Key |
| --- | --- | --- | --- | --- | --- |
| 0 | id | INTEGER | No | None | Yes |
| 1 | staff_name | TEXT | Yes | None | No |
## STAFF_PICK

| ID | Name | Type | Not Null | Default Value | Primary Key |
| --- | --- | --- | --- | --- | --- |
| 0 | id | INTEGER | No | None | Yes |
| 1 | staff_id | INTEGER | Yes | None | No |
| 2 | book_id | INTEGER | Yes | None | No |
| 3 | pick_blurb | TEXT | Yes | None | No |
## TOP_FIVE

| ID | Name | Type | Not Null | Default Value | Primary Key |
| --- | --- | --- | --- | --- | --- |
| 0 | id | INTEGER | No | None | Yes |
| 1 | staff_id | INTEGER | Yes | None | No |
| 2 | book_id | INTEGER | Yes | None | No |
| 3 | year | INTEGER | Yes | None | No |
| 4 | rank | INTEGER | Yes | None | No |
