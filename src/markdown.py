from src.database import Database


class Markdown:
    def __init__(self, database: Database):
        super().__init__()

        self.database = database

    def get(self, schema: str, relation_type: str) -> str | None:
        if schema not in self.database.schemas:
            return None

        self.database.select_schema(schema)

        markdown = f"# {schema} table statement\n\n"
        table_names = self.database.table_names
        # TODO : table sort by table name

        for table_name in table_names:
            table_short_name = self.database.get_table_short_name(table_name)

            markdown += f"## {table_short_name} \n\n"

            desc = self.database.get_table_comment(table_name)

            markdown += f"**Description:** {desc}\n\n" if desc else ""

            markdown += f"| Column | Type | Not null | PK | FK | Description |\n"
            markdown += "|---|---|---|---|---|---|\n"
            for column in self.database.get_columns(table_name):
                column_type = type(column.type).__name__
                if hasattr(column.type, "length"):
                    column_type = f"{column_type}({column.type.length})"

                pk = 'O' if column.name in self.database.get_primary_keys(table_name) else ''
                not_nullable = 'O' if not column.nullable else ''

                if relation_type == 'laravel':
                    fk = 'O' if self.database.is_foreign_key_laravel(column.name) else ''
                else:
                    fk = 'O' if column.name in self.database.get_foreign_keys(table_name) else ''

                line = f"| {column.name} |"\
                   f" {column_type} |"\
                   f" {not_nullable} |"\
                   f" {pk} |" \
                   f" {fk} |" \
                   f" {column.comment if column.comment else ''} |"

                markdown += line + "|\n"

            markdown += "\n"

        return markdown
