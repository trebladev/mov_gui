# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from PySide6 import QtGui
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
from tools.findimg import get_cover
import sys
import os
import time

i = 1
Qlist = []
slm = QStringListModel()
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        # self.item_list = []

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon": "icon_file.svg",
            "btn_id": "open_page_2",
            "btn_text": "open_page_2",
            "btn_tooltip": "open_page_2",
            "show_top": True,
            "is_active": False
        }
    ]

     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # DELETE BEFORE DATA
        os.system("rm -rf scene*")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD CUSTOM THEMES
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # LOAD
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # ADD INIT FUNCTION
        # ///////////////////////////////////////////////////////////////

        # ADD INIT LIST
        self.item_list = []
        self.image_path = []
        self.ui.load_pages.big_scene.setChecked(True)
        self.ui.load_pages.small_scene.setChecked(False)

        # INIT LABEL 2 SHOW GRAPH
        self.pix = QtGui.QPixmap("img/bigscene.png")
        size = self.pix.size()
        self.ui.load_pages.page1_label.setGeometry(0, 0, 584, 574)
        self.ui.load_pages.page1_label.setScaledContents(True)
        self.ui.load_pages.page1_label.setPixmap(self.pix)

        self.pix = QtGui.QPixmap("img/noimage.png")

        self.ui.load_pages.page2_label.setGeometry(0, 0, 584, 574)
        self.ui.load_pages.page2_label.setScaledContents(True)
        self.ui.load_pages.page2_label.setPixmap(self.pix)


        # ADD CUSTOM BUTTON
        self.page1_st_btn = PyPushButton(
            text="????????????",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )

        self.page2_st_btn  = PyPushButton(
            text="????????????",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )

        self.page2_cp_btn  = PyPushButton(
            text="????????????",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )

        def callback_st_1():

            self.page1_st_btn.setText("????????????")
            # print("dwwd")
            #time.sleep(2)
            os.system("./fastfusion/FastFusionV2 -c ./fastfusion/calib.txt -op ./data/scene_origin"+str(i))
            # self.page1_st_btn.setText("")
            # time.sleep(2)
            #self.page1_st_btn.setText("????????????")
            self.image_path.append(get_cover("./scene_origin"+str(i)))
            show_graph(self.ui.load_pages.page1_label,self.image_path[i-1])
            add_scan_item()
            self.page1_st_btn.setText("????????????")


        def callback_cp_1():
            # self.page2_cp_btn.setText("????????????")
            select = self.ui.load_pages.page2_list.selectedIndexes()
            if(not select):
                print("not select")
                msg_box = QMessageBox(QMessageBox.Critical, 'ERROR', 'no scene was selected')
                msg_box.exec_()
            else:
                os.system("./moving_object_detection/movable_object_detection -c ./moving_object_detection/config.json -np /home/iipl/PyOneDark_Qt_Widgets_Modern_GUI/scene_changed/mesh.obj -op /home/iipl/PyOneDark_Qt_Widgets_Modern_GUI/scene_origin"+str(select[0].row()+1)+"/mesh.obj")
            # self.page2_cp_btn.setText("????????????")

        def callback_st_2():
            #self.page2_st_btn.setText("????????????")
            # time.sleep(2)
            # os.system(
            #     "/media/gty/hhh/CLionProjects/FastFusion_obec_show/cmake-build-release/Apps/FastFusion/FastFusionV2 /me
            # ia / gty / hhh / CLionProjects / FastFusion_obec_show / Files / Azurekinect / calib.txt
            # ")
            os.system("./fastfusion/FastFusionV2 -c ./fastfusion/calib.txt -op ./scene_changed")


            #self.page2_st_btn.setText("????????????")

        def changename():
            self.page1_st_btn.setText("????????????")
        def add_scan_item():
            global i
            global Qlist
            # print(f'Qlist: {Qlist}')
            # Qlist.append("item " + str(i))
            self.item_list.append("??????"+str(i))
            i += 1
            show_scan_list()
            print(f'add_scan_item item list: {self.item_list}')

        def show_scan_list():

            # print(Qlist)
            # print(i)

            # self.qList = Qlist
            # slm.setStringList(self.qList)
            slm.setStringList(self.item_list)
            self.ui.load_pages.scan_list.setModel(slm)
            self.ui.load_pages.page2_list.setModel(slm)

        def list_save():
            # self.qList = slm.stringList()
            # Qlist = slm.stringList()
            self.item_list = slm.stringList()
            print(f'item list: {self.item_list}')

        def show_graph(label,image_path):
            self.pix = QtGui.QPixmap(image_path)
            label.setPixmap(self.pix)

        def choose_scene_img():
            # select = self.ui.load_pages.scan_list.selectedItem()
            select = self.ui.load_pages.scan_list.selectedIndexes()
            # print(select[0].row())
            show_graph(self.ui.load_pages.page1_label,self.image_path[select[0].row()])

        def show_origin_img():
            select = self.ui.load_pages.page2_list.selectedIndexes()
            show_graph(self.ui.load_pages.page2_label,self.image_path[select[0].row()])

        def check_big():
            show_graph(self.ui.load_pages.page1_label,"img/bigscene.png")

        def check_small():
            show_graph(self.ui.load_pages.page1_label,"img/smallscene.png")

            
        self.page2_st_btn.setMinimumHeight(40)
        self.page2_cp_btn.setMinimumHeight(40)

        # ADD TO LAYOUT
        self.ui.load_pages.start_btn_layout.addWidget(self.page1_st_btn)
        self.ui.load_pages.page2_btn_layout.addWidget(self.page2_st_btn)
        self.ui.load_pages.page2_btn_layout.addWidget(self.page2_cp_btn)

        self.page1_st_btn.clicked.connect(callback_st_1)
        self.page2_cp_btn.clicked.connect(callback_cp_1)
        self.page2_st_btn.clicked.connect(callback_st_2)
        slm.dataChanged.connect(list_save)
        self.ui.load_pages.scan_list.clicked.connect(choose_scene_img)
        self.ui.load_pages.page2_list.clicked.connect(show_origin_img)
        self.ui.load_pages.big_scene.clicked.connect(check_big)
        self.ui.load_pages.small_scene.clicked.connect(check_small)





        # ADD GRAPH FUNCTION
        # ///////////////////////////////////////////////////////////////



        # show_graph(self.ui.load_pages.page1_label,"abc-124.jpg")
        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)