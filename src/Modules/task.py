from datetime import datetime
today_date = datetime.now().strftime('%Y-%m-%d %H:%M')
class Task:
    def __init__(self, name: str, end: int, status: bool) -> None:
        self._name = name
        self._end = end
        self._status = status

    def get_deadline(self)-> str:
        return self._end
    
    def change_date(self, new_date:str) -> None:
        self._end = new_date
        
    def get_name(self) -> str:
        return self._name
    
    def get_status(self) -> bool:
        return self._status
    
    def change_status(self) -> None:
        self._status = not self._status
    
    def is_deadline_passed(self) -> bool:
        return datetime.now() < datetime.strptime(self.get_deadline(), "%Y-%m-%d %H:%M")
    