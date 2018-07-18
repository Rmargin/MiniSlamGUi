#!/bin/python
#coding:utf-8

# Copyright (c) 2008,Runzhu Wang, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Runzhu Wang, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

import wx
#imort other lib python test, lib in systeam
import os
#wildcard
wildcard = u"Python 文件 (*.py)|*.py|"  "All files (*.*)|*.*|"   "Bag files(*.bag)|*.bag|"    "Pbstream files(*.pbstream)|*.pbstream|"

class HelloFrame(wx.Frame):
    """
    A Frame that Test Cartographer GUI to show
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)
        
        # create a panel in the frame
        pnl = wx.Panel(self)
        
        #class value to do  get index
        self.slam_bag_file = []
        self.slam_trajectory_pbstream_file = []
        #blank string clear buffer is long long
        self.balck_string = ''
        
        #SlAM pose_graph path
        self.pose_graph_config_path = "/home/wangrz/workspace/workcode/Carto2018-04-18/src/cartographer/configuration_files"

        #init TextCtral
        text = wx.TextCtrl(pnl, value = '',pos=(110,153), size =(550, 20), style = wx.TE_CENTER)
        text = wx.TextCtrl(pnl, value = '',pos=(110,183), size =(550, 20), style = wx.TE_CENTER)
        
        # create miniGUI Information header
        # and put some text with a larger bold font on it
        st = wx.StaticText(pnl, label="SLAM MiniGUI", pos=(120,5)) #set some text windows param to show
        font = st.GetFont()
        font.PointSize += 10
        #font = font.Bold()
        st.SetFont(font)

        #launch model
        # creat miniGUI offline data to display
        st = wx.StaticText(pnl, label="--- Launch SLAM ---", pos=(30,65)) #set some text windows param to show
        font = st.GetFont()
        font.PointSize += 1
        #font = font.Bold()
        st.SetFont(font)
        
        # creat miniGUI offline data to display
        st = wx.StaticText(pnl, label="--- Offline SLAM ---", pos=(30,130)) #set some text windows param to show
        font = st.GetFont()
        font.PointSize += 1
        #font = font.Bold()
        st.SetFont(font)
        
        #create configure
        st = wx.StaticText(pnl, label="--- Configure SLAM ---", pos=(30,315)) #set some text windows param to show
        font = st.GetFont()
        font.PointSize += 1
        #font = font.Bold()
        st.SetFont(font)
        
        #create wxpython windows botton object test and bing event
        #creat button keyword
        self.loadbtn = wx.Button(pnl,label="Run",pos=(25,85),size=(80,25))
        self.closebtn = wx.Button(pnl,label="Close",pos=(165,85),size=(80,25))
        self.Savebtn = wx.Button(pnl,label="Save",pos=(305,85),size=(80,25))
        
        #open rosbag floder
        self.Foldertn = wx.Button(pnl,label="BagFolder",pos=(435,85),size=(80,25))
        self.Bind(wx.EVT_BUTTON, self.onFolder_button,self.Foldertn)
        
        #bing event
        self.Bind(wx.EVT_BUTTON, self.onRun_button, self.loadbtn)
        self.loadbtn.SetDefault()

        self.Bind(wx.EVT_BUTTON, self.onClose_button, self.closebtn)
        self.closebtn.SetDefault()

        self.Bind(wx.EVT_BUTTON, self.onSave_button, self.Savebtn)
        self.closebtn.SetDefault()

        self.option_offlin_bag = wx.Button(pnl,label="OpenBag",pos=(25,150),size=(80,25)) 
        self.Bind(wx.EVT_BUTTON, self.OnButton_option_file_bag,self.option_offlin_bag)

        self.option_offlin_pbstream = wx.Button(pnl,label="OpenPb",pos=(25,180),size=(80,25)) 
        self.Bind(wx.EVT_BUTTON, self.OnButton_option_file_pbstream,self.option_offlin_pbstream)

        self.option_offlin_display  = wx.Button(pnl,label="Redisplay",pos=(25,230),size=(80,25)) 
        self.Bind(wx.EVT_BUTTON, self.OnButton_redisplay,self.option_offlin_display)

        self.option_offlin_ply = wx.Button(pnl,label="PlyPoint",pos=(25,260),size=(80,25)) 
        self.Bind(wx.EVT_BUTTON, self.OnButton_plypoint,self.option_offlin_ply)

        #config
        self.config_3D_slam = wx.Button(pnl,label="Cfg3D",pos=(25,335),size=(80,25)) 
        self.Bind(wx.EVT_BUTTON, self.OnButton_config_3D_slam,self.config_3D_slam)

        self.config_assets_writer = wx.Button(pnl,label="CfgPly",pos=(165,335),size=(80,25)) 
        self.Bind(wx.EVT_BUTTON, self.OnButton_config_assets_writer,self.config_assets_writer)

        self.rebuild = wx.Button(pnl,label="Rebuild",pos=(305,335),size=(80,25)) 
        self.Bind(wx.EVT_BUTTON, self.OnButton_rebuild,self.rebuild)
        
        self.Pose_Graphtn = wx.Button(pnl,label="CfgPose",pos=(25,375),size=(80,25))
        self.Bind(wx.EVT_BUTTON, self.onPoseGraph_button,self.Pose_Graphtn)

        self.Tracjectory_3Dtn = wx.Button(pnl,label="CfgTra3D",pos=(165,375),size=(80,25))
        self.Bind(wx.EVT_BUTTON, self.onTrajectory3D_button,self.Tracjectory_3Dtn)

        #panel = wx.Panel(self, -1)
        self.panel = pnl
 
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to Cartograper Slam!")

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
    
    #create button keyworld function test "run Cartographer GUI"
    def onRun_button( self, event):
        """Run Cartographer cammand to run in linux"""
        self.loadbtn.SetLabel("noRun")
        os.system('./run')

    def onClose_button( self, event):
        """ Close runin Slam prohram function"""
        self.closebtn.SetLabel("onClose")
        os.system('exit') # exit all terminal as same time  exit slam

    def onSave_button( self, event):
        """Save imu Velodyne_points data current folder"""
        self.Savebtn.SetLabel("onSave")
        os.system('./savebag')

    def onFolder_button( self, event):
        """Open rosbag folder"""
        self.Foldertn.SetLabel("onfolder")
        os.system('nautilus ~/Slam_bag')
    
    def OnButton_config_3D_slam( self, event):
        """config 3D slam """
        self.config_3D_slam.SetLabel("OK!")
        os.system('gedit /home/wangrz/workspace/workcode/Carto2018-04-18/src/cartographer_ros/cartographer_ros/configuration_files/backpack_3d.lua')
    
    def OnButton_config_assets_writer( self, event):
        """Open rosbag folder"""
        self.config_assets_writer.SetLabel("OK!")
        os.system('gedit /home/wangrz/workspace/workcode/Carto2018-04-18/src/cartographer_ros/cartographer_ros/configuration_files/assets_writer_backpack_3d.lua')
    
    def OnButton_rebuild( self, event):
        """Open rosbag folder"""
        self.rebuild.SetLabel("OK!")
        os.system('catkin_make_isolated --use-ninja')

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def onPoseGraph_button( self, event):
        """Slam3D configure pose_graph"""
        self.Pose_Graphtn.SetLabel("OK!")
        os.system('gedit '+self.pose_graph_config_path+'/pose_graph.lua')
        #print check program
        print 'ok! open pose_graph configure file'
    
    def onTrajectory3D_button( self, event):
        """Slam3D configure Trajecotry3D"""
        self.Tracjectory_3Dtn.SetLabel("OK!")
        os.system('gedit '+self.pose_graph_config_path+'/trajectory_builder_3d.lua')
        #print check program 
        print 'ok! open Trajectory 3D configure'

    #----------------------------------------------------------------------  
    def OnButton_option_file_bag(self, event):
        """ open bag file  and  to product"""
        dlg = wx.FileDialog(self,message="option file",  
                            defaultDir=os.getcwd(),  
                            defaultFile="",  
                            wildcard=wildcard,  
                            style=wx.OPEN|wx.MULTIPLE|wx.CHANGE_DIR)  
          
        if dlg.ShowModal() == wx.ID_OK:  
            paths = dlg.GetPaths()
            
            #setup blank string to clear buffer
            #center = wx.StaticText(self.panel,-1,self.balck_string,(110,153),(2000,1000),wx.ALIGN_CENTER)
            #then you can
            #center = wx.StaticText(self.panel,-1,paths[0],(110,153),(2000,1000),wx.ALIGN_CENTER)
            
            #TextCtrl compars StaticText
            text = wx.TextCtrl(self.panel, value = paths[0],pos=(110,153), size =(550, 20), style = wx.TE_CENTER)
            print paths
            
            #save global
            self.slam_bag_file = paths 
            print paths
            for path in paths:
                print path
          
        dlg.Destroy()  
        
    #----------------------------------------------------------------------  
    def OnButton_option_file_pbstream(self, event):  
        """ open bag and pstream to product """  
        dlg = wx.FileDialog(self,message="option file",  
                            defaultDir=os.getcwd(),  
                            defaultFile="",  
                            wildcard=wildcard,  
                            style=wx.OPEN|wx.MULTIPLE|wx.CHANGE_DIR)  
          
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            #you can frist setup blanK to clear buffer
            #center = wx.StaticText(self.panel,-1,self.balck_string,(110,183),(2000,1000),wx.ALIGN_CENTER)
            #then you can 
            #center = wx.StaticText(self.panel,-1,paths[0],(110,183),(2000,1000),wx.ALIGN_CENTER) 

            #TextCtrl compars StaticText
            text = wx.TextCtrl(self.panel, value = paths[0],pos=(110,183), size =(550, 20), style = wx.TE_CENTER)

            print paths

            self.slam_trajectory_pbstream_file = paths
            for path in paths:
                print path
                
    #---------------------------------------------------------------------
    def OnButton_redisplay(self, event):
        """replay rosbag data make cartographer product pbstream."""
        #source cartographer path to setup env
        os.system('source devel_isolated/setup.bash')
        #launch cartographer offline program
        os.system('roslaunch cartographer_ros offline_my_backpack.launch bag_filenames:='+self.slam_bag_file[0])
        #test shell cammand to do get it
        print ('roslaunch cartographer_ros offline_my_backpack.launch bagfilenames:='+self.slam_bag_file[0])
        
    def OnButton_plypoint(self, event):
        """of course you have cartographer pbstream you can product ply file."""
        #launch slam assets_writer get ply but you have to get .bag and .pstream file
        
        #source cartographer path to setup env
        os.system('source devel_isolated/setup.bash')

        #launch cartographer offline program
        os.system('roslaunch cartographer_ros assets_writer_backpack_3d.launch  \
        bag_filenames:='+self.slam_bag_file[0] + ' ' + 'pose_graph_filename:=' + self.slam_trajectory_pbstream_file[0])
        
        #test shell cammand to do get it
        print ('roslaunch cartographer_ros assets_writer_backpack_3d.launch \
        bag_filenames:='+self.slam_bag_file[0] + ' ' + 'pose_graph_filename:=' + self.slam_trajectory_pbstream_file[0])

    #--------------------------------------------------------------------
    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython,weus")

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a slam sample",
                      "About test lidar slam ",
                      wx.OK|wx.ICON_INFORMATION)

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = HelloFrame(None, title='Test SlAM MINIGUI') #windows named  by self
    frm.SetSize( wx.Size( 680, 500 ) ) 
    frm.Show()
    app.MainLoop()

