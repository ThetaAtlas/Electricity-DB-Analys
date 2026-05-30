import sqlite3
import os
from smolagents import Tool
from pathlib import Path


class DatabaseQueryTool(Tool): 
    name = "query_energy_market_db"
    description = """Execute SQL queries on the local energy_market.db database for Texas electricity market data.
    
Available tables: dim_date, fact_electricity_price, fact_breakeven_inflation, fact_energy_volatility.
Always JOIN with dim_date on date_id for time queries.
Only SELECT allowed."""

    #links to project directory than database folder so no hard links
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    target_path = project_root / "data_base" / "energy_market.db"
    
    #telling the AI what it can send 
    inputs = {                                      #command
        "sql_query": {                              #definition
            "type": "string",                       #what data type that data definition is
            "description": "Valid SQL SELECT query" #Tells AI only send select queries
        }
    }
    output_type = "string"

    def __init__(self):
        super().__init__()

        self.db_path = self.target_path
        
    def forward(self, sql_query: str) -> str:
        if not os.path.exists(self.db_path):
            return f"Database file not found at: {self.db_path}\nPlease check the file location."

        try:
            #connects to database using sqlite3
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            #prevents unsafe commands
            upper = sql_query.upper().strip()
            if any(cmd in upper for cmd in ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "CREATE"]):
                return "Only SELECT queries allowed for safety."

            #Execute query
            cursor.execute(sql_query)
            results = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description] if cursor.description else []

            #error if not handle is found
            if not results:
                return " Query successful. No rows returned."

            #Creates fancy fun header for table calls once
            output = f"**Results** ({len(results)} rows):\n\n"
            output += "| " + " | ".join(columns) + " |\n"
            output += "| " + "---|" * len(columns) + "\n"

            #Limits to first fifty responses then adds this to the options string
            for row in results[:50]:
                output += "| " + " | ".join(str(x) for x in row) + " |\n" #\n means new line so it hits enter after evrey entry

            #case where there are more than fifty basicly slaps on a there are more and calls it a day
            if len(results) > 50:
                output += f"\n... + {len(results)-50} more rows."

            #close database
            conn.close()
            #return answers and print them
            return output

        #if something explodes we just throw an error out there
        except Exception as e:
            return f"Database Error: {str(e)}"