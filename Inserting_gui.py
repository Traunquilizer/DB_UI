<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>563</width>
    <height>328</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Приём заявок</string>
  </property>
  <property name="locale">
   <locale language="Russian" country="Russia"/>
  </property>
  <widget class="QWidget" name="centralWidget">
   <widget class="QLabel" name="lab_start_phone">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>170</y>
      <width>21</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>+7</string>
    </property>
   </widget>
   <widget class="QDateEdit" name="dateEdit">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>220</y>
      <width>110</width>
      <height>21</height>
     </rect>
    </property>
    <property name="autoFillBackground">
     <bool>false</bool>
    </property>
    <property name="currentSection">
     <enum>QDateTimeEdit::DaySection</enum>
    </property>
    <property name="displayFormat">
     <string>d/M/yy</string>
    </property>
    <property name="calendarPopup">
     <bool>true</bool>
    </property>
    <property name="timeSpec">
     <enum>Qt::LocalTime</enum>
    </property>
   </widget>
   <widget class="QLabel" name="lab_stuff">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>100</y>
      <width>131</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Примечания</string>
    </property>
   </widget>
   <widget class="QLabel" name="lab_phone">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>150</y>
      <width>131</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Телефон</string>
    </property>
   </widget>
   <widget class="QLabel" name="lab_product_name">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>50</y>
      <width>131</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Название изделия</string>
    </property>
   </widget>
   <widget class="QLabel" name="lab_date">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>200</y>
      <width>131</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Дата</string>
    </property>
   </widget>
   <widget class="QPushButton" name="button_proceed">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>270</y>
      <width>261</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Принять в ремонт</string>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="textf_stuff">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>120</y>
      <width>261</width>
      <height>121</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="lab_receiver">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>250</y>
      <width>131</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Принял</string>
    </property>
   </widget>
   <widget class="QPushButton" name="button_search">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>20</y>
      <width>211</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Поиск по базе</string>
    </property>
   </widget>
   <widget class="QLabel" name="lab_name">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>100</y>
      <width>131</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>ФИО</string>
    </property>
   </widget>
   <widget class="QComboBox" name="cBox_receiver">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>270</y>
      <width>121</width>
      <height>21</height>
     </rect>
    </property>
    <property name="maxVisibleItems">
     <number>3</number>
    </property>
    <item>
     <property name="text">
      <string>Дик А.И.</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Бруй В.И.</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Шаповалова Н.А.</string>
     </property>
    </item>
   </widget>
   <widget class="QLineEdit" name="line_product_name">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>70</y>
      <width>251</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="line_name">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>120</y>
      <width>251</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="line_phone">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>170</y>
      <width>231</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QCheckBox" name="checkBox_guarantee">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>70</y>
      <width>131</width>
      <height>22</height>
     </rect>
    </property>
    <property name="text">
     <string>Гарантия</string>
    </property>
   </widget>
  </widget>
 </widget>
 <layoutdefault spacing="6" margin="11"/>
 <tabstops>
  <tabstop>line_product_name</tabstop>
  <tabstop>checkBox_guarantee</tabstop>
  <tabstop>line_name</tabstop>
  <tabstop>line_phone</tabstop>
  <tabstop>dateEdit</tabstop>
  <tabstop>cBox_receiver</tabstop>
  <tabstop>button_proceed</tabstop>
  <tabstop>button_search</tabstop>
  <tabstop>textf_stuff</tabstop>
 </tabstops>
 <resources/>
 <connections/>
</ui>
