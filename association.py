screen_nav = """

ScreenManager:
    MenuScreen:
    RegiWindo:
    Loginwindo:
    MangerLog:
    TeacherLog:
    MangerDuser:
    MangerMakeTeacher:
    MyProfile:
    PassReset:
    Change_Name:
    Change_DOB:
    StudentPage:
    Sprofile:
    GradesPage:
    ChangeSgrade:
    reportprob:
    ManagClass:
    annonman:
    pageann:
    viewsch:
    clsspress:
    clsch:


<MenuScreen>:
    name:'menu'

    MDRectangleFlatButton:
        text:'Log In'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint:0.5,0.2
        on_release:
            root.manager.current='Login'
    MDRectangleFlatButton:
        text:'Sign Up'
        pos_hint:{'center_x':0.5,'center_y':0.2}
        size_hint:0.5,0.2
        on_release:
            root.manager.current='Register'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        title: 'Welcome to School App'
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:8
                    Widget:          
        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation:'vertical'

                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'sce.jpg'


                MDLabel:
                    text:'  Welcome '
                    font_style:'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Log in'
                            on_press:
                                root.manager.current='Login'
                            IconLeftWidget:
                                icon:'login'
                        OneLineIconListItem:
                            text:'Report a problem'
                            on_press:
                                root.manager.current='report'
                            IconLeftWidget:
                                icon:'account-alert'                               
                        OneLineIconListItem:
                            text:'Sign Up'
                            on_press:
                                root.manager.current='Register'
                            IconLeftWidget:
                                icon:'face-woman'
                        OneLineIconListItem:
                            text:'viewPage'
                            on_press:
                                root.manager.current='clsh'
                            IconLeftWidget:
                                icon:'account-box'

                        OneLineIconListItem:
                            text:'Announcements'
                            on_press:
                                root.manager.current='pageann'
                            IconLeftWidget:
                                icon:'account-box'

<RegiWindo>
    name:'Register'
    id_box:idnum
    fullname_box:f_name
    dob:date
    username_box:username
    password_box:pass_word

    MDToolbar:
        title: 'Register'
        elevation: 10
        pos_hint: {'top': 1}
    MDTextField:
        hint_text:"ID number"
        pos_hint:{'center_x':0.5,'center_y':0.7}
        size_hint_x:None
        width:300
        id:idnum
        multiline:False
    MDTextField:
        hint_text:"Full Name"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300
        id:f_name
        multiline:False
    MDTextField:
        hint_text:"date of birth(dd/mm/yyyy)"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
        id:date
        multiline:False
    MDTextField:
        hint_text:"Username"
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint_x:None
        width:300
        id:username
        multiline:False
    MDTextField:
        hint_text:"Password"
        pos_hint:{'center_x':0.5,'center_y':0.3}
        size_hint_x:None
        width:300
        id:pass_word
        password:True
        multiline:False
    MDRectangleFlatButton:
        text:'Submit'
        pos_hint:{'center_x':0.3,'center_y':0.2} 
        width:300
        on_release:
            root.regibtn()
    MDRectangleFlatButton:
        text:'Cancel'
        pos_hint:{'center_x':0.8,'center_y':0.2} 
        width:300
        on_release:
            root.manager.current='menu'

<Loginwindo>
    name:'Login'
    username_box:username
    password_box:pass_word
    id:container
    MDToolbar:
        title: 'Log In'
        elevation: 10

    MDTextField:
        hint_text:"Username"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300
        id:username
        multiline:False
    MDTextField:
        hint_text:"Password"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
        id:pass_word
        password:True
        multiline:False

    MDRectangleFlatButton:
        text:'Log In'
        pos_hint:{'center_x':0.3,'center_y':0.4} 
        width:300
        on_release:
            root.logbtn()

    MDRectangleFlatButton:
        text:'Cancel'
        pos_hint:{'center_x':0.8,'center_y':0.3} 
        width:300
        on_release:
            root.manager.current='menu'    
    MDRectangleFlatButton:
        text:'Reset Password'
        pos_hint:{'center_x':0.8,'center_y':0.2} 
        width:300
        on_release:
            root.manager.current='Preset'


<MangerLog>
    name:'mangerlog'
    id:currentuser

    MDRectangleFlatButton:
        text:'Make Teacher'
        pos_hint:{'center_x':0.9,'top':0.8}
        size_hint:0.2,0.2
        on_release:
            root.manager.current='MangerMakeTeacher'

    MDRectangleFlatButton:
        text:'Delete User'
        pos_hint:{'center_x':0.9,'top':0.6}
        size_hint:0.2,0.2
        on_release:
            root.manager.current='MangerDuser'

    MDRectangleFlatButton:
        text:'Change schedual'
        pos_hint:{'center_x':0.9,'top':0.4}
        size_hint:0.2,0.2
        on_press:
            root.manger_log()        

    MDRectangleFlatButton:
        text:'Make announcement'
        pos_hint:{'center_x':0.9,'top':0.2}
        size_hint:0.2,0.2 
        on_release:
            root.manager.current='annopage'


    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        id:managertoolbar
                        title:
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:8
                    Widget:          
        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation:'vertical'

                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'sce.jpg'


                MDLabel:
                    text:'  Welcome'
                    font_style:'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Profile'
                            on_release:
                                root.my_profile() 
                            IconLeftWidget:
                                icon:'face-profile'
                        OneLineIconListItem:
                            text:'My Messages'
                            IconLeftWidget:
                                icon:'message'
                        OneLineIconListItem:
                            text:'Home Page'
                            on_press:
                                root.home_button()
                            IconLeftWidget:
                                icon:'home'  
                        OneLineIconListItem:
                            text:'Announcement'
                            on_press:
                                root.my_anno()
                            IconLeftWidget:
                                icon:'android-messages'                               
                        OneLineIconListItem:
                            text:'Log Out'
                            on_press:
                                root.manager.current='menu'
                            IconLeftWidget:
                                icon:'logout'


<TeacherLog>
    name:'teacherlog'


    MDRectangleFlatButton:
        text:'Presence Check'
        pos_hint:{'center_x':0.9,'top':0.8}
        size_hint:0.2,0.2
        on_release:
            root.studpress()
    MDRectangleFlatButton:
        text:'change grade'
        pos_hint:{'center_x':0.9,'top':0.6}
        size_hint:0.2,0.2
        on_release:
            root.S_grades()

    MDRectangleFlatButton:
        text:'Remove student'
        pos_hint:{'center_x':0.9,'top':0.4}
        size_hint:0.2,0.2

    MDRectangleFlatButton:
        text:'Add Assignment'
        pos_hint:{'center_x':0.9,'top':0.2}
        size_hint:0.2,0.2




    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        id:teachername
                        title:
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:8
                    Widget:          
        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation:'vertical'

                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'sce.jpg'


                MDLabel:
                    text:'  Welcome '
                    font_style:'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Profile'
                            on_release:
                                root.my_profile()                             
                            IconLeftWidget:
                                icon:'face-profile'
                        OneLineIconListItem:
                            text:'My Messages'
                            IconLeftWidget:
                                icon:'message'
                        OneLineIconListItem:
                            text:'Home Page'
                            on_press:
                                root.home_button()
                            IconLeftWidget:
                                icon:'home'    
                        OneLineIconListItem:
                            text:'Announcement'
                            on_press:
                                root.my_anno()
                            IconLeftWidget:
                                icon:'android-messages'                          
                        OneLineIconListItem:
                            text:'Log Out'
                            on_press:
                                root.manager.current='menu'
                            IconLeftWidget:
                                icon:'logout'

<MangerDuser>
    name:"MangerDuser"
    idnum:idnumber
    MDToolbar:
        title: 'Delete User'
        elevation: 10
        pos_hint: {'top': 1}

    MDTextField:
        hint_text:"Enter the user ID you want to delete"
        pos_hint:{'center_x':0.4,'center_y':0.5}
        size_hint_x:None
        width:300
        id:idnumber
        multiline:False
    MDRectangleFlatButton:
        text:'Confirm'
        pos_hint:{'center_x':0.2,'center_y':0.2} 
        size_hint:0.3,0.3
        on_release:
            root.deletebtn()
    MDRectangleFlatButton:
        text:'Back'
        pos_hint:{'center_x':0.6,'center_y':0.2} 
        size_hint:0.3,0.3
        on_release:
            root.manager.current='mangerlog' 

<MangerMakeTeacher>
    name:"MangerMakeTeacher"
    identity:IDnum
    subject:Sub
    MDToolbar:
        title: 'Make teacher'
        elevation: 10
        pos_hint: {'top': 1}

    MDTextField:
        hint_text:"Enter User ID number"
        pos_hint:{'center_x':0.4,'center_y':0.6}
        size_hint_x:None
        width:300
        id:IDnum
        multiline:False
    MDTextField:
        hint_text:"Enter Subject"
        pos_hint:{'center_x':0.4,'center_y':0.4}
        size_hint_x:None
        width:300
        id:Sub
        multiline:False
    MDRectangleFlatButton:
        text:'Back'
        pos_hint:{'center_x':0.6,'center_y':0.2} 
        size_hint:0.2,0.2
        on_release:
            root.manager.current='mangerlog'
    MDRectangleFlatButton:
        text:'Confirm'
        pos_hint:{'center_x':0.2,'center_y':0.2} 
        size_hint:0.2,0.2
        on_release:
            root.MkTeacher()
            root.manager.current='mangerlog'


<MyProfile>
    name:"myprofile"      
    MDToolbar:
        id:thisUser
        title: 'My Profile'
        elevation: 10
        pos_hint: {'top': 1}
    MDLabel:
        id:name
        text:
        pos_hint:{'center_x':0.5,'center_y':0.7}
        size_hint_x:None
        width:300
    MDLabel:
        id:username
        text:
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300
    MDLabel:
        id:idnum
        text:
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
    MDLabel:
        id:dob
        text:
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint_x:None
        width:300
    MDLabel:
        id:subt
        text:
        pos_hint:{'center_x':0.5,'center_y':0.3}
        size_hint_x:None
        width:300

    MDRectangleFlatButton:
        text:'Change'
        pos_hint:{'center_x':0.8,'center_y':0.7} 
        width:300
        on_release:
            root.manager.current='chname'

    MDRectangleFlatButton:
        text:'Change'
        pos_hint:{'center_x':0.8,'center_y':0.4} 
        width:300
        on_release:
            root.manager.current='chdob'              


    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        id:test
                        title: 'My Profile'
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:8
                    Widget:          
        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation:'vertical'

                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'sce.jpg'


                MDLabel:
                    text:'  Welcome'
                    font_style:'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Profile'
                            on_release:
                                root.manager.current='myprofile'             
                            IconLeftWidget:
                                icon:'face-profile'

                        OneLineIconListItem:
                            text:'Home Page'
                            on_press:
                                root.home_button()
                            IconLeftWidget:
                                icon:'home'                                 
                        OneLineIconListItem:
                            text:'Log Out'
                            on_press:
                                root.manager.current='menu'
                            IconLeftWidget:
                                icon:'logout'
<PassReset>
    name:'Preset'
    MDToolbar:
        title: 'Password Reset'
        elevation: 10
        pos_hint: {'top': 1}        
    MDTextField:
        hint_text:"Enter User ID number"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300
        id:IDnum
        multiline:False
    MDTextField:
        hint_text:"Enter User Date of Birth"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
        id:dob
        multiline:False
    MDTextField:
        hint_text:"Enter New Password"
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint_x:None
        width:300
        id:newpass
        password:True
        multiline:False

    MDRectangleFlatButton:
        text:'Confirm'
        pos_hint:{'center_x':0.3,'center_y':0.2} 
        size_hint:0.2,0.2
        on_release:
            root.resetPass()

    MDRectangleFlatButton:
        text:'Cancel'
        pos_hint:{'center_x':0.6,'center_y':0.2} 
        size_hint:0.2,0.2
        on_release:
            root.manager.current='menu'                             
<Change_Name>
    name:"chname"
    id:changeName
    MDLabel:
        id:username
        text:
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300    
    MDToolbar:

        title: 'Change Name'
        elevation: 10
        pos_hint: {'top': 1}

    MDTextField:
        hint_text:"Enter your new name"
        pos_hint:{'center_x':0.4,'center_y':0.5}
        size_hint_x:None
        width:300
        id:newname
        multiline:False
    MDRectangleFlatButton:
        text:'Confirm'
        pos_hint:{'center_x':0.2,'center_y':0.2} 
        size_hint:0.3,0.3
        on_release:
            root.change_name()
    MDRectangleFlatButton:
        text:'Back'
        pos_hint:{'center_x':0.6,'center_y':0.2} 
        size_hint:0.3,0.3
        on_release:
            root.back_button()

<Change_DOB>
    name:"chdob"
    MDLabel:
        id:username
        text:
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300    
    MDToolbar:

        title: 'Change DOB'
        elevation: 10
        pos_hint: {'top': 1}

    MDTextField:
        hint_text:"Enter your Date of birth"
        pos_hint:{'center_x':0.4,'center_y':0.5}
        size_hint_x:None
        width:300
        id:newdob
        multiline:False
    MDRectangleFlatButton:
        text:'Confirm'
        pos_hint:{'center_x':0.2,'center_y':0.2} 
        size_hint:0.3,0.3
        on_release:
            root.change_DOB()
    MDRectangleFlatButton:
        text:'Back'
        pos_hint:{'center_x':0.6,'center_y':0.2} 
        size_hint:0.3,0.3
        on_release:
            root.back_button()
<Sprofile>
    name:"Sprofile"     
    MDToolbar:
        id:thisUser
        title: 'My Profile'
        elevation: 10
        pos_hint: {'top': 1}
    MDLabel:
        id:name
        text:
        pos_hint:{'center_x':0.5,'center_y':0.7}
        size_hint_x:None
        width:300
    MDLabel:
        id:username
        text:
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300
    MDLabel:
        id:idnum
        text:
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
    MDLabel:
        id:dob
        text:
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint_x:None
        width:300
    MDLabel:
        id:subt
        text:
        pos_hint:{'center_x':0.5,'center_y':0.3}
        size_hint_x:None
        width:300           


    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        id:test
                        title: 'My Profile'
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:8
                    Widget:          
        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation:'vertical'

                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'sce.jpg'


                MDLabel:
                    text:'  Welcome'
                    font_style:'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Profile'
                            on_release:
                                root.manager.current='Sprofile'             
                            IconLeftWidget:
                                icon:'face-profile'
                        OneLineIconListItem:
                            text:'Home Page'
                            on_press:
                                root.home_button()
                            IconLeftWidget:
                                icon:'home'                                 
                        OneLineIconListItem:
                            text:'Log Out'
                            on_press:
                                root.manager.current='menu'
                            IconLeftWidget:
                                icon:'logout'

<StudentPage>
    name:'Spage'
    id:currentuser
    MDRectangleFlatButton:
        text:'Send Message'
        pos_hint:{'center_x':0.9,'top':0.8}
        size_hint:0.2,0.2


    MDRectangleFlatButton:
        text:'My Grades'
        pos_hint:{'center_x':0.9,'top':0.6}
        size_hint:0.2,0.2
        on_release:
            root.my_grades() 


    MDRectangleFlatButton:
        text:'My schedule'
        pos_hint:{'center_x':0.9,'top':0.4}
        size_hint:0.2,0.2
        on_release:
            root.showsh()
        
    MDRectangleFlatButton:
        text:'Submit Assignment'
        pos_hint:{'center_x':0.9,'top':0.2}
        size_hint:0.2,0.2

    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        id:studenttoolbar
                        title:
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:8
                    Widget:          
        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation:'vertical'

                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'sce.jpg'


                MDLabel:
                    id:username
                    text:
                    font_style:'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Profile'
                            on_release:
                                root.my_profile() 
                            IconLeftWidget:
                                icon:'face-profile'
                        OneLineIconListItem:
                            text:'My Grades'
                            on_release:
                                root.my_grades() 
                            IconLeftWidget:
                                icon:'clipboard-list'
                        OneLineIconListItem:
                            text:'My Messages'
                            IconLeftWidget:
                                icon:'message'
                        OneLineIconListItem:
                            text:'Home Page'
                            on_press:
                                root.home_button()
                            IconLeftWidget:
                                icon:'home'
                        OneLineIconListItem:
                            text:'Announcement'
                            on_press:
                                root.my_anno()
                            IconLeftWidget:
                                icon:'android-messages'
                        OneLineIconListItem:
                            text:'Schedule'
                            on_press:
                                root.showsh()
                            IconLeftWidget:
                                icon:'school'                                        
                        OneLineIconListItem:
                            text:'Log Out'
                            on_press:
                                root.manager.current='menu'
                            IconLeftWidget:
                                icon:'logout'
<GradesPage>
    name:'grades'

    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        id:stdentgradebar
                        title:
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:8
                    ScrollView:
                        MDList:
                            id:grades
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation:'vertical'

                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'sce.jpg'


                MDLabel:
                    id:username
                    text:
                    font_style:'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Home Page'
                            on_press:
                                root.home_button()
                            IconLeftWidget:
                                icon:'home'                                 
                        OneLineIconListItem:
                            text:'Log Out'
                            on_press:
                                root.manager.current='menu'
                            IconLeftWidget:
                                icon:'logout'
<ChangeSgrade>
    name:'chgrades'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        title:'Change Student Grade'
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:8
                    BoxLayout:
                        ScrollView:
                            MDList:
                                id:grades
                    BoxLayout:
                        MDTextField:
                            hint_text:"Enter the student ID"
                            pos_hint:{'center_x':0.4,'center_y':0.5}
                            size_hint_x:None
                            width:300
                            id:studentid
                            multiline:False
                        MDTextField:
                            hint_text:"Enter the the student new grade"
                            pos_hint:{'center_x':0.4,'center_y':0.5}
                            size_hint_x:None
                            width:300
                            id:newgrade
                            multiline:False
                        MDRectangleFlatButton:
                            text:'Confirm'
                            pos_hint:{'center_x':0.2,'center_y':0.2} 
                            size_hint:0.3,0.3
                            on_release:
                                root.change_grade()
                        MDRectangleFlatButton:
                            text:'Back'
                            pos_hint:{'center_x':0.6,'center_y':0.2} 
                            size_hint:0.3,0.3
                            on_release:
                                root.home_button()
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation:'vertical'

                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'sce.jpg'


                MDLabel:
                    id:username
                    text:
                    font_style:'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:

                        OneLineIconListItem:
                            text:'Home Page'
                            on_press:
                                root.home_button()
                            IconLeftWidget:
                                icon:'home'                                 
                        OneLineIconListItem:
                            text:'Log Out'
                            on_press:
                                root.manager.current='menu'
                            IconLeftWidget:
                                icon:'logout'         

<reportprob>
    name:'report'
    emailtxt:remail
    msgtxt:retext
    MDRectangleFlatButton:
        text:'<'
        pos_hint:{'center_x':0.05,'center_y':0.95}
        size_hint:0.05,0.05
        on_press:
            root.manager.current='menu'
    MDTextField:
        hint_text:"Enter your Email"
        pos_hint:{'center_x':0.4,'center_y':0.8}
        size_hint_x:None
        width:300
        id:remail
        multiline:False
    MDTextField:
        hint_text:"Enter your problem here"
        pos_hint:{'center_x':0.4,'center_y':0.5}
        size_hint_x:None
        width:500
        id:retext
        multiline:True

    MDRectangleFlatButton:
        text:'Send'
        pos_hint:{'center_x':0.8,'center_y':0.2}
        size_hint:0.5,0.2
        on_press:
            root.printtxt()
    MDRectangleFlatButton:
        text:'Reset'
        pos_hint:{'center_x':0.2,'center_y':0.2}
        size_hint:0.5,0.2
        on_press:
            remail.text=""
            retext.text=""    


<ManagClass>
    name:'manclass'
    id:menuday
    id:menutime
    MDTextField:
        id:timepicked
    MDTextField:
        id:daypicked
    BoxLayout:
        MDToolbar:
            title:'Class Schedule'
            elevation: 10
            pos_hint: {'bottom': 1} 
    BoxLayout:    
        BoxLayout:
            orientation:'horizontal'
            BoxLayout:
                orientation:'horizontal'
                BoxLayout:
                    ScrollView:
                        MDList:
                            id:menuday
                BoxLayout:
                    ScrollView:
                        MDList:
                            id:menutime

        BoxLayout:
            orientation:'horizontal'
            BoxLayout:           
                MDTextField:
                    hint_text:"Enter Teacher ID"
                    pos_hint:{'center_x':0.5,'center_y':0.4}
                    size_hint_x:None
                    width:300
                    id:idt
                    multiline:False
            BoxLayout:        
                MDTextField:
                    hint_text:"Class ID"
                    pos_hint:{'center_x':0,'center_y':0.3}
                    size_hint_x:None
                    width:300
                    id:classid
                    multiline:False
            BoxLayout:        
                MDRectangleFlatButton:
                    text:'Submit'
                    pos_hint:{'center_x':0.5,'center_y':0.2} 
                    width:300
                    on_release:
                        root.data_submit()
            BoxLayout:        
                MDRectangleFlatButton:
                    text:'Back'
                    pos_hint:{'center_x':0.2,'center_y':0.2} 
                    width:300
                    on_release:
                        root.manager.current='mangerlog'



<annonman>
    name:'annopage'
    anntext:annid
    MDToolbar:
        title:'announcement page'
        elevation: 10
        pos_hint: {'top': 1}
    MDRectangleFlatButton:
        text:'<'
        pos_hint:{'center_x':0.05,'center_y':0.8}
        size_hint:0.05,0.05
        on_press:
            root.manager.current='mangerlog'
    MDTextField:
        hint_text:"Announcement"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
        id:annid
        multiline:True
    MDRectangleFlatButton:
        text:'Post'
        pos_hint:{'center_x':0.6,'center_y':0.2} 
        width:300
        on_release:
            root.send_anno()
    MDRectangleFlatButton:
        text:'Reset'
        pos_hint:{'center_x':0.3,'center_y':0.2} 
        width:300
        on_release:
            annid.text=''

<pageann>
    name:'pageann'
    MDLabel:
        id:reanno
        text:
        pos_hint:{'center_x':0.5,'center_y':0.7}
        size_hint_x:None
        width:300
    MDLabel:
        id:retime
        text:
        pos_hint:{'center_x':0.5,'center_y':0.8}
        size_hint_x:None
        width:300
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        id:studenttoolbar
                        title:
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:8
                    Widget:          
        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation:'vertical'

                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'sce.jpg'


                MDLabel:
                    text:'Announcement From School Principal'
                    font_style:'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Home Page'
                            on_press:
                                root.home_button()
                            IconLeftWidget:
                                icon:'home'                                      
                        OneLineIconListItem:
                            text:'Log Out'
                            on_press:
                                root.manager.current='menu'
                            IconLeftWidget:
                                icon:'logout'


<viewsch>
    name:'views'


<clsspress>
    name:'clssp'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        title:'Present Check'
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:8
                    BoxLayout:
                        ScrollView:
                            MDList:
                                id:studlist

                    Widget:

        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation:'vertical'

                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'sce.jpg'


                MDLabel:
                    id:username
                    text:
                    font_style:'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Home Page'
                            on_press:
                                root.home_button()
                            IconLeftWidget:
                                icon:'home'                                 
                        OneLineIconListItem:
                            text:'Log Out'
                            on_press:
                                root.manager.current='menu'
                            IconLeftWidget:
                                icon:'logout'   



<clsch>
    name:'clsh'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        title:'Present Check'
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:8
                    BoxLayout:
                        ScrollView:
                            MDList:
                                id:sun

                        ScrollView:
                            MDList:
                                id:mon

                        ScrollView:
                            MDList:
                                id:tue

                        ScrollView:
                            MDList:
                                id:wed

                        ScrollView:
                            MDList:
                                id:thu






        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation:'vertical'

                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'sce.jpg'



                ScrollView:
                    MDList:

                        OneLineIconListItem:
                            text:'Home Page'
                            on_press:
                                root.home_button()
                            IconLeftWidget:
                                icon:'home'                                 
                        OneLineIconListItem:
                            text:'Log Out'
                            on_press:
                                root.manager.current='menu'
                            IconLeftWidget:
                                icon:'logout'   

"""