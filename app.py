from PySide2 import QtWidgets
from movie import get_movies
class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cine Club Application")
        self.setup_ui()
        self.populate_movies()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie  = QtWidgets.QPushButton("Add a movie")
        self.lw_movies = QtWidgets.QListWidget()
        self.btn_removeMovies = QtWidgets.QPushButton("Remove movie(s)")

        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovies)
    
    def populate_movies(self):
        movies = get_movies()
        for movie in movies:
            self.lw_movies.addItem(movie.title)

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
