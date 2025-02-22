# models/room.py

from database.db_connection import get_connection

class RoomModel:
    @staticmethod
    def create_room(room_number, room_type, price_per_night, status='Available'):
        """
        Insert a new room record into the Rooms table.
        """
        conn = get_connection()
        cursor = conn.cursor()
        try:
            insert_query = """
                INSERT INTO Rooms (room_number, room_type, price_per_night, status)
                VALUES (:room_number, :room_type, :price_per_night, :status)
            """
            cursor.execute(insert_query, {
                "room_number": room_number,
                "room_type": room_type,
                "price_per_night": price_per_night,
                "status": status
            })
            conn.commit()
            print("Room created successfully!")
        except Exception as e:
            print("Error creating room:", e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_room(room_id):
        """
        Retrieve a room record by room_id.
        """
        conn = get_connection()
        cursor = conn.cursor()
        try:
            select_query = "SELECT * FROM Rooms WHERE room_id = :room_id"
            cursor.execute(select_query, {"room_id": room_id})
            room = cursor.fetchone()
            return room  # returns a tuple (room_id, room_number, room_type, price_per_night, status)
        except Exception as e:
            print("Error retrieving room:", e)
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_room(room_id, room_number=None, room_type=None, price_per_night=None, status=None):
        """
        Update fields of an existing room record.
        """
        conn = get_connection()
        cursor = conn.cursor()
        try:
            update_query = "UPDATE Rooms SET "
            update_fields = []
            params = {}

            if room_number:
                update_fields.append("room_number = :room_number")
                params["room_number"] = room_number
            if room_type:
                update_fields.append("room_type = :room_type")
                params["room_type"] = room_type
            if price_per_night is not None:
                update_fields.append("price_per_night = :price_per_night")
                params["price_per_night"] = price_per_night
            if status:
                update_fields.append("status = :status")
                params["status"] = status

            update_query += ", ".join(update_fields)
            update_query += " WHERE room_id = :room_id"
            params["room_id"] = room_id

            cursor.execute(update_query, params)
            conn.commit()
            print("Room updated successfully!")
        except Exception as e:
            print("Error updating room:", e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_room(room_id):
        """
        Delete a room record from the Rooms table.
        """
        conn = get_connection()
        cursor = conn.cursor()
        try:
            delete_query = "DELETE FROM Rooms WHERE room_id = :room_id"
            cursor.execute(delete_query, {"room_id": room_id})
            conn.commit()
            print("Room deleted successfully!")
        except Exception as e:
            print("Error deleting room:", e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
