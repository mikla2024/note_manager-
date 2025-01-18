import sqlite3



def delete_note_from_db(note_id: int, db_path: str):

    connection = sqlite3.connect(db_path)
    crsr = connection.cursor()

    sql_str = (
        f'DELETE FROM notes WHERE id = {note_id}'
    )

    crsr.execute(sql_str)
    connection.commit()
    connection.close()

if __name__ == '__main__':

    delete_note_from_db(3, '../note_manager.db')