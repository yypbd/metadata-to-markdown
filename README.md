
# MetaData To ERD

## Description

This is a tool that automatically generates Database Table Statement using SQLAlchemy's MetaData.

## Features

## Installation

### compose env

- copy .env.sample to .env
- write DATABASE_URL in SQLAlchemy url string.

```dotenv
# postgresql
DATABASE_URL="postgresql+pg8000://<<username>>:<<password>>@<<host>>:<<port>>/<<dbname>>"
```

```dotenv
# mysql
DATABASE_URL="mysql+pymysql://<<username>>:<<passwored>>@<<host>>:<<port>>/<<dbname>>?charset=utf8mb4"
```

## Usages

### show_schemas

```bash
uv run main.py show_schemas
```

### generate_markdown

```bash
uv run main.py generate_erd \
  --schema=<<schema>> \
  --relation_type=laravel \
  --out_filename=out.md  
```

## Options

### generate_markdown options

| option            | Type     | Value           | Description                                                |
|-------------------|----------|-----------------|------------------------------------------------------------|
| schema            | String   |                 | Database schema name.                                      |
| relation_type     | String   | none<br>laravel | none: Read database FK<br>laravel: laravel migration style |
| out_filename      | String   |                 | markdown filename                                          |

## Links

### SQLAlchemy

- [SQLAlchemy Dialects](https://docs.sqlalchemy.org/en/20/dialects/index.html)

## Samples
