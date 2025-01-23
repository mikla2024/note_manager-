import sqlite3



def delete_note_from_db(note_id: int, db_path: str, io_table='notes', my_cn: sqlite3.Connection = None):

    if not my_cn:
        with sqlite3.connect(db_path) as cn:
            crsr = cn.cursor()
    else:
        crsr = my_cn.cursor()

    sql_str = (
        f'DELETE FROM {io_table} WHERE id = {note_id}'
    )

    crsr.execute(sql_str)
    crsr.connection.commit()

if __name__ == '__main__':

    delete_note_from_db(3, '../note_manager.db')