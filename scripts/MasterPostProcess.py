"""
Rail Projects Post Process - This script adds the VRLID to project status updates,...and updates relevant domains.
It is based on a series of scripts exported from Model Builder.

Created/Updated By: Rick Scott
Create Date: 01/07/2015

Change Log

"""
import adodbapi
import arcpy
import sys
import os
#import smtplib
import datetime
import time
#from email.mime.text import MIMEText

print "Beginning script..."

startTime = datetime.datetime.now()

with open("C://Connections.txt","r") as Conn:
    lines = Conn.readlines()

for line in lines:
    if line[0:1]!="#":
        if "sdeDDev = " in line:
            sdeDDev = line[line.index("= \"")+3:len(line)-2]
            #print sdeDDev
        elif "sdeRail = " in line:
            sdeRail = line[line.index("= \"")+3:len(line)-2]
            #print sdeRail
        elif "ConsultantPM_txt" in line:
            ConsultantPM_txt = line[line.index("= \"")+3:len(line)-2]
            #print ConsultantPM_txt
        elif "VTransPM_txt" in line:
            VTransPM_txt = line[line.index("= \"")+3:len(line)-2]
            #print VTransPM_txt
        elif "Consultants_txt" in line:
            Consultants_txt = line[line.index("= \"")+3:len(line)-2]
            #print Consultants_txt
        elif "ConsultantsContact_txt" in line:
            ConsultantsContact_txt = line[line.index("= \"")+3:len(line)-2]
            #print ConsultantsContact_txt
        elif "ProjectType_txt" in line:
            ProjectType_txt = line[line.index("= \"")+3:len(line)-2]
            #print ProjectType_txt
        elif "LocationType_txt" in line:
            LocationType_txt = line[line.index("= \"")+3:len(line)-2]
            #print LocationType_txt            
        elif "VRLID_join_csv" in line:
            VRLID_join_csv = line[line.index("= \"")+3:len(line)-2]
            #print VRLID_join_csv
        elif "AssetType_txt" in line:
            AssetType_txt = line[line.index("= \"")+3:len(line)-2]
            #print AssetType_txt
        elif "AllPMs_txt" in line:
            AllPMs_txt = line[line.index("= \"")+3:len(line)-2]
            #print AllPMs_txt
        elif "ProjectDescription_txt" in line:
            ProjectDescription_txt = line[line.index("= \"")+3:len(line)-2]
            #print ProjectDescription_txt
        elif "Status_Update_WebFC" in line:
            DDEV_Status_Update_WebFC = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            RAIL_Status_Update_WebFC = sdeRail + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_Status_Update_WebFC
            #print RAIL_Status_Update_WebFC
        elif "PROJ_Status_Updates__Table_" in line:
            DDEV_PROJ_Status_Updates_Table = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_PROJ_Status_Updates_Table
        elif "dev_gdb_Projects_Backup" in line:
            dev_gdb_Projects_Backup = line[line.index("= \"")+3:len(line)-2]
            #print dev_gdb_Projects_Backup
        elif "GDB_Projects_Table" in line:
            DDEV_Projects_Table = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            RAIL_Projects_Table = sdeRail + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_Projects_Table
            #print RAIL_Projects_Table
        elif "Add_Project_WebFC" in line:
            DDEV_Add_Project_WebFC = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            RAIL_Add_Project_WebFC = sdeRail + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_Add_Project_WebFC
            #print RAIL_Add_Project_WebFC            
        elif "PROJ_Projects_View1" in line:
            DDEV_PROJ_Projects_View1 = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_PROJ_Projects_View1
        elif "PROJ_Projects_View2" in line:
            DDEV_PROJ_Projects_View2 = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_PROJ_Projects_View2
        elif "PROJ_Projects_View3" in line:
            DDEV_PROJ_Projects_View3 = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_PROJ_Projects_View3
        elif "PROJ_Projects_View4" in line:
            DDEV_PROJ_Projects_View4 = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_PROJ_Projects_View4
        elif "PROJ_Projects_View5" in line:
            DDEV_PROJ_Projects_View5 = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_PROJ_Projects_View5
        elif "PROJ_Projects_View6" in line:
            DDEV_PROJ_Projects_View6 = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_PROJ_Projects_View6            
        elif "PROJ_Projects_Status_Updates_View1" in line:
            DDEV_PROJ_Projects_Status_Updates_View1 = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_PROJ_Projects_View1
        elif "PROJ_Projects_Status_Updates_View2" in line:
            DDEV_PROJ_Projects_Status_Updates_View2 = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_PROJ_Projects_View2
        elif "PROJ_Projects_Status_Updates_View3" in line:
            DDEV_PROJ_Projects_Status_Updates_View3 = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_PROJ_Projects_View3
        elif "PROJ_Projects_Status_Updates_View4" in line:
            DDEV_PROJ_Projects_Status_Updates_View4 = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_PROJ_Projects_View4            
        elif "AssetID" in line:
            RAIL_AssetID = sdeRail + "/" + line[line.index("= \"")+3:len(line)-2]
            #print RAIL_AssetID
        elif "RailConn" in line:
            RailConn = line[line.index("= \"")+3:len(line)-2]
            #print RailConn
        elif "Rail_LRS" in line:
            Rail_LRS = sdeRail + "/" + line[line.index("= \"")+3:len(line)-2]
            #print RAIL_AssetID
        elif "Project_Points_FC" in line:
            DDEV_Project_Points_FC = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            #print Project_Points_FC
        elif "Project_Lines_FC" in line:
            DDEV_Project_Lines_FC = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_Project_Lines_FC            
        elif "PROJ_Points_PROJ_StatusUpdates_REL" in line:
            DDEV_PROJ_Points_PROJ_StatusUpdates_REL = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_PROJ_Points_PROJ_StatusUpdates_REL            
        elif "PROJ_Lines_PROJ_StatusUpdates_REL" in line:
            DDEV_PROJ_Lines_PROJ_StatusUpdates_REL = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-1]
            #print DDEV_PROJ_Lines_PROJ_StatusUpdates_REL 
        else:
            pass

        domainAssociations = []

def CalcVRLIDs():
    try:
# Local variables:
        global DDEV_Add_Project_WebFC
        global DDEV_Projects_Table
        global DDEV_AssetID
        global DDEV_PROJ_Projects_View1
        global DDEV_PROJ_Projects_View2

# Process: Add Project web fc table view
        arcpy.MakeTableView_management(DDEV_Add_Project_WebFC, DDEV_PROJ_Projects_View1)

# Process: Append add project to project table
        arcpy.Append_management(DDEV_PROJ_Projects_View1, DDEV_Projects_Table, "NO_TEST")

# Process: project table view
        arcpy.MakeTableView_management(DDEV_Projects_Table, DDEV_PROJ_Projects_View2)

# Process: join to asset ID
        arcpy.AddJoin_management(DDEV_PROJ_Projects_View2, "AssetID", RAIL_AssetID, "AssetID", "KEEP_COMMON")

#DEBUGGING:  Determining field names based on join
##        fields = arcpy.ListFields(DDEV_PROJ_Projects_View2)
##        for field in fields:
##            print("{0} is a type of {1} with a length of {2}"
##              .format(field.name, field.type, field.length))

# Process: calculate VRLID
        arcpy.CalculateField_management(DDEV_PROJ_Projects_View2, "VRLID", "!GDB_Rail.RAIL_ADMIN.ASSET_ID_SCHEMA.VRLID!", "PYTHON", "")

    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)

def dynSegAddProjects():
    try:
# Local variables:
        global DDEV_Add_Project_WebFC
        global DDEV_Projects_Table
        global DDEV_AssetID
        global DDEV_PROJ_Projects_View3
        global DDEV_PROJ_Projects_View4
        global DDEV_PROJ_Projects_View5
        global Rail_LRS
        
# Process: Make Table View
        print "dynSegAddProjects:  Creating first table view for appending LRS attributes to project data..."
        arcpy.MakeTableView_management(DDEV_Projects_Table, DDEV_PROJ_Projects_View3) 

        
# Process: Join project table to Rail LRS
        print "dynSegAddProjects:  Joining first table view to LRS for appending attributes to project data..."
        arcpy.AddJoin_management(DDEV_PROJ_Projects_View3, "VRLID", Rail_LRS, "VRLID", "KEEP_ALL")

##        fields = arcpy.ListFields(DDEV_PROJ_Projects_View3)
##        for field in fields:
##            print("{0} is a type of {1} with a length of {2}"
##              .format(field.name, field.type, field.length))

        print "dynSegAddProjects:  Appending LRS attributes to project data..."
# Process: Calculate LineName
        arcpy.CalculateField_management(DDEV_PROJ_Projects_View3, "LineName", "!GDB_Rail.RAIL_ADMIN.INV_Rail_LRS.LineName!", "PYTHON", "")

# Process: Calculate Operator
        arcpy.CalculateField_management(DDEV_PROJ_Projects_View3, "Operator", "!GDB_Rail.RAIL_ADMIN.INV_Rail_LRS.Operator!", "PYTHON", "")

# Process: Calculate Division
        arcpy.CalculateField_management(DDEV_PROJ_Projects_View3, "Division", "!GDB_Rail.RAIL_ADMIN.INV_Rail_LRS.Division!", "PYTHON", "")

# Process: Calculate Subdivision
        arcpy.CalculateField_management(DDEV_PROJ_Projects_View3, "Subdivision", "!GDB_Rail.RAIL_ADMIN.INV_Rail_LRS.Subdivision!", "PYTHON", "")

# Process: Calculate Branch
        arcpy.CalculateField_management(DDEV_PROJ_Projects_View3, "Branch", "!GDB_Rail.RAIL_ADMIN.INV_Rail_LRS.Branch!", "PYTHON", "")

# Process: Calculate StateOwned
        arcpy.CalculateField_management(DDEV_PROJ_Projects_View3, "StateOwned", "!GDB_Rail.RAIL_ADMIN.INV_Rail_LRS.StateOwned!", "PYTHON", "")

# Process: Calculate RailTrail
        arcpy.CalculateField_management(DDEV_PROJ_Projects_View3, "RailTrail", "!GDB_Rail.RAIL_ADMIN.INV_Rail_LRS.RailTrail!", "PYTHON", "")

# Process: Query projects table - points
        print "dynSegAddProjects:  Creating second table view for generating project point data..."
        arcpy.MakeTableView_management(DDEV_Projects_Table, DDEV_PROJ_Projects_View4, "ToMP IS NULL")

        
# Process: Dynseg points
        print "dynSegAddProjects:  DynSegging second table view to in-memory point layer..."
        lyrPoints = "Point Events"
        arcpy.MakeRouteEventLayer_lr(Rail_LRS, "VRLID", DDEV_PROJ_Projects_View4, "VRLID POINT FromMP", lyrPoints)
                   
# Process: Project points to FC
        if arcpy.Exists(sdeDDev + "/PROJ_Points"):
            arcpy.Delete_management(sdeDDev + "/PROJ_Points")
    
        print "dynSegAddProjects:  Saving in-memory point layer to GDB..."
        arcpy.FeatureClassToFeatureClass_conversion(lyrPoints, sdeDDev, "PROJ_Points")

# Process: Add Fields
        print "dynSegAddProjects:  Adding version tracking fields to new point FC..."
        arcpy.AddField_management(sdeDDev + "/PROJ_Points", "created_user", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(sdeDDev + "/PROJ_Points", "created_date", "DATE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(sdeDDev + "/PROJ_Points", "last_edited_user", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(sdeDDev + "/PROJ_Points", "last_edited_date", "DATE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Query projects table - lines
        print "dynSegAddProjects:  Creating third table view for generating project line data..."        
        arcpy.MakeTableView_management(DDEV_Projects_Table, DDEV_PROJ_Projects_View5, "ToMP IS NOT NULL")

        print "dynSegAddProjects:  There are potentially " + str(arcpy.GetCount_management(DDEV_PROJ_Projects_View5)) + " polylines in the data..."

# Process: Dynseg points
        print "dynSegAddProjects:  DynSegging third table view to in-memory line layer..."
        lyrLines = "Line Events"
        arcpy.MakeRouteEventLayer_lr(Rail_LRS, "VRLID", DDEV_PROJ_Projects_View5, "VRLID LINE FromMP ToMP", lyrLines)

        print "dynSegAddProjects:  " + str(arcpy.GetCount_management(lyrLines)) + " polylines  were created..."

# Process: Project lines to FC
        if arcpy.Exists(sdeDDev + "/PROJ_Lines"):
            arcpy.Delete_management(sdeDDev + "/PROJ_Lines")
        print "dynSegAddProjects:  Saving in-memory line layer to GDB..."
        arcpy.FeatureClassToFeatureClass_conversion(lyrLines, sdeDDev, "PROJ_Lines")

# Process: Add Fields
        print "dynSegAddProjects:  Adding version tracking fields to new line FC..."
        arcpy.AddField_management(sdeDDev + "/PROJ_Lines", "created_user", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(sdeDDev + "/PROJ_Lines", "created_date", "DATE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(sdeDDev + "/PROJ_Lines", "last_edited_user", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(sdeDDev + "/PROJ_Lines", "last_edited_date", "DATE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Update projects domain from add project FC
        print "dynSegAddProjects:  Updating project name domain with new projects..."
        arcpy.TableToDomain_management(DDEV_Add_Project_WebFC, "ProjectName", "ProjectName", sdeDDev, "ProjectName", "ProjectName", "APPEND")

# Process: Delete Rows
        print "dynSegAddProjects:  Clean out Collector 'new projects' FC for new projects..."
        arcpy.DeleteRows_management(DDEV_Add_Project_WebFC)

    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)

def statusUpdatesAppend():
    try:
        global DDEV_Status_Update_WebFC
        global DDEV_PROJ_Status_Updates_Table
        global DDEV_PROJ_Projects_Status_Updates_View1

        #Status update web FC table view
        print "statusUpdateAppend:  Creating table view for appending new project status data to master..."        
        arcpy.MakeTableView_management(DDEV_Status_Update_WebFC, DDEV_PROJ_Projects_Status_Updates_View1)

        print "statusUpdateAppend: There are " + str(arcpy.GetCount_management(DDEV_PROJ_Projects_Status_Updates_View1)) + " status updates available to append..."

        #Append status web FC to status table
        print "statusUpdateAppend:  Appending new project status data to master..."
        arcpy.Append_management(DDEV_PROJ_Projects_Status_Updates_View1, DDEV_PROJ_Status_Updates_Table, "NO_TEST")
        
    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)

def dynSegStatusUpdates():
    try:
        global sdeDDev
        global DDEV_Projects_Table
        global Rail_LRS
        global DDEV_PROJ_Status_Updates_Table
        global DDEV_PROJ_Projects_Status_Updates_View2
        global DDEV_PROJ_Projects_Status_Updates_View3
        global DDEV_PROJ_Projects_Status_Updates_View4
        global DDEV_PROJ_Projects_View6

        #Make Table Views of project and project status masters for joining
        print "dynSegStatusUpdates:  Creating project and project status table views for joining..."
        arcpy.MakeTableView_management(DDEV_PROJ_Status_Updates_Table, DDEV_PROJ_Projects_Status_Updates_View2)
        arcpy.MakeTableView_management(DDEV_Projects_Table, DDEV_PROJ_Projects_View6)        

        #Join project status to projects
        print "dynSegStatusUpdates:  Joining project status to project table views in order to calculate rail lrs values..."
        arcpy.AddJoin_management(DDEV_PROJ_Projects_Status_Updates_View2, "ProjectName", DDEV_PROJ_Projects_View6, "ProjectName", "KEEP_COMMON")        

        print "dynSegStatusUpdates:  Appending LRS attributes to project status data..." 
        #Calculate Field VRLID into project status
        arcpy.CalculateField_management(DDEV_PROJ_Projects_Status_Updates_View2, "VRLID", "!GDB_DDev.DDev_ADMIN.PROJ_Projects.VRLID!", "PYTHON", "")

        #Calculate Field FromMP into project status
        arcpy.CalculateField_management(DDEV_PROJ_Projects_Status_Updates_View2, "FromMP", "!GDB_DDev.DDev_ADMIN.PROJ_Projects.FromMP!", "PYTHON", "")

        #Calculate Field ToMP into project status
        arcpy.CalculateField_management(DDEV_PROJ_Projects_Status_Updates_View2, "ToMP", "!GDB_DDev.DDev_ADMIN.PROJ_Projects.ToMP!", "PYTHON", "")

        #Make Table View of project status master for point dyn seg
        print "dynSegStatusUpdates:  Creating project status table views for creating point events..."
        arcpy.MakeTableView_management(DDEV_PROJ_Status_Updates_Table, DDEV_PROJ_Projects_Status_Updates_View3, "ToMP IS NULL")

        print "dynSegAddProjects:  There are " + str(arcpy.GetCount_management(DDEV_PROJ_Projects_Status_Updates_View3)) + " records in the table view for points..."
        
        #Make Route Event Point Layer project status table view
        print "dynSegStatusUpdates:  Creating point events..."
        Point_Events = "lyrPoints"
        arcpy.MakeRouteEventLayer_lr(Rail_LRS, "VRLID", DDEV_PROJ_Projects_Status_Updates_View3, "VRLID POINT FromMP", Point_Events)

        print "dynSegAddProjects:  There are " + str(arcpy.GetCount_management(Point_Events)) + " points in the in-memory data..."

        if arcpy.Exists(sdeDDev + "/PROJ_StatusPoints"):
            arcpy.Delete_management(sdeDDev + "/PROJ_StatusPoints")

        #Copy in-memory point feature layer to GDB
        print "dynSegStatusUpdates:  Copying in-memory point feature layer to GDB..."
        arcpy.FeatureClassToFeatureClass_conversion(Point_Events, sdeDDev, "PROJ_StatusPoints", "", "ProjectName \"Project Name\" true true true 100 Text 0 0 ,First,#,RAIL_ADMIN Events,ProjectName,-1,-1;Status \"Status Update\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,Status,-1,-1;Action \"Action Items\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,Action,-1,-1;LatestConstEst \"Latest Construction Estimate w/ E&C\" true true false 8 Double 8 38 ,First,#,RAIL_ADMIN Events,LatestConstEst,-1,-1;EnvAllClear \"Environmental All Clear\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,EnvAllClear,-1,-1;UtilClear \"Utilities Clearance\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,UtilClear,-1,-1;ROWClear \"ROW Clearance\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,ROWClear,-1,-1;RRClear \"Railroad Clearance\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,RRClear,-1,-1;AdvertiseTarget \"Project Advertisement Target\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,AdvertiseTarget,-1,-1;ProjectManager \"Updating Project Manager (Your Name)\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,ProjectManager,-1,-1;created_user \"created_user\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,created_user,-1,-1;created_date \"created_date\" true true false 36 Date 0 0 ,First,#,RAIL_ADMIN Events,created_date,-1,-1;last_edited_user \"last_edited_user\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,last_edited_user,-1,-1;last_edited_date \"last_edited_date\" true true false 36 Date 0 0 ,First,#,RAIL_ADMIN Events,last_edited_date,-1,-1;VRLID \"VRLID\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,VRLID,-1,-1;FromMP \"FromMP\" true true false 8 Double 8 38 ,First,#,RAIL_ADMIN Events,FromMP,-1,-1;ToMP \"ToMP\" true true false 8 Double 8 38 ,First,#,RAIL_ADMIN Events,ToMP,-1,-1", "")

        #Make Table View of project status master for line dyn seg
        print "dynSegStatusUpdates:  Creating project status table views for creating line events..."
        arcpy.MakeTableView_management(DDEV_PROJ_Status_Updates_Table, DDEV_PROJ_Projects_Status_Updates_View4, "ToMP IS NOT NULL")

        print "dynSegAddProjects:  There are " + str(arcpy.GetCount_management(DDEV_PROJ_Projects_Status_Updates_View4)) + " records in the table view for lines..."

        #Make Route Event Line Layer project status table view
        print "dynSegStatusUpdates:  Creating line events..."
        Line_Events = "lyrLines"
        arcpy.MakeRouteEventLayer_lr(Rail_LRS, "VRLID", DDEV_PROJ_Projects_Status_Updates_View4, "VRLID LINE FromMP ToMP", Line_Events)

        print "dynSegAddProjects:  There are " + str(arcpy.GetCount_management(Line_Events)) + " lines in the in-memory data..."

        if arcpy.Exists(sdeDDev + "/PROJ_StatusLines"):
            arcpy.Delete_management(sdeDDev + "/PROJ_StatusLines")            

        #Copy in-memory line feature layer to GDB
        print "dynSegStatusUpdates:  Copying in-memory line feature layer to GDB..."
        arcpy.FeatureClassToFeatureClass_conversion(Line_Events, sdeDDev, "PROJ_StatusLines", "", "ProjectName \"Project Name\" true true true 100 Text 0 0 ,First,#,RAIL_ADMIN Events,ProjectName,-1,-1;Status \"Status Update\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,Status,-1,-1;Action \"Action Items\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,Action,-1,-1;LatestConstEst \"Latest Construction Estimate w/ E&C\" true true false 8 Double 8 38 ,First,#,RAIL_ADMIN Events,LatestConstEst,-1,-1;EnvAllClear \"Environmental All Clear\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,EnvAllClear,-1,-1;UtilClear \"Utilities Clearance\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,UtilClear,-1,-1;ROWClear \"ROW Clearance\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,ROWClear,-1,-1;RRClear \"Railroad Clearance\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,RRClear,-1,-1;AdvertiseTarget \"Project Advertisement Target\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,AdvertiseTarget,-1,-1;ProjectManager \"Updating Project Manager (Your Name)\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,ProjectManager,-1,-1;created_user \"created_user\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,created_user,-1,-1;created_date \"created_date\" true true false 36 Date 0 0 ,First,#,RAIL_ADMIN Events,created_date,-1,-1;last_edited_user \"last_edited_user\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,last_edited_user,-1,-1;last_edited_date \"last_edited_date\" true true false 36 Date 0 0 ,First,#,RAIL_ADMIN Events,last_edited_date,-1,-1;VRLID \"VRLID\" true true false 255 Text 0 0 ,First,#,RAIL_ADMIN Events,VRLID,-1,-1;FromMP \"FromMP\" true true false 8 Double 8 38 ,First,#,RAIL_ADMIN Events,FromMP,-1,-1;ToMP \"ToMP\" true true false 8 Double 8 38 ,First,#,RAIL_ADMIN Events,ToMP,-1,-1", "")

    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)

def projStatusRelates():
    try:
        global DDEV_Project_Points_FC        
        global DDEV_Project_Lines_FC
        global DDEV_PROJ_Status_Updates_Table
        global DDEV_PROJ_Points_PROJ_StatusUpdates_REL
        global DDEV_PROJ_Lines_PROJ_StatusUpdates_REL

        # Process: Point-Status relationship
        arcpy.CreateRelationshipClass_management(DDEV_Project_Points_FC, DDEV_PROJ_Status_Updates_Table, DDEV_PROJ_Points_PROJ_StatusUpdates_REL, "SIMPLE", DDEV_PROJ_Status_Updates_Table, DDEV_Project_Points_FC, "NONE", "ONE_TO_MANY", "NONE", "ProjectName", "ProjectName", "", "")
        # Process: Line-Status relationship
        arcpy.CreateRelationshipClass_management(DDEV_Project_Lines_FC, DDEV_PROJ_Status_Updates_Table, DDEV_PROJ_Lines_PROJ_StatusUpdates_REL, "SIMPLE", DDEV_PROJ_Status_Updates_Table, DDEV_Project_Lines_FC, "NONE", "ONE_TO_MANY", "NONE", "ProjectName", "ProjectName", "", "")

    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)



def disconnectDomains(obj):
    try:
        global domainAssociations
#Remove domain from their associated fields.  Domains association with fields prevent those domains from being deleted.
        fields = arcpy.ListFields(obj)
        for field in fields:
            #desc = arcpy.Describe(field)
            if len(field.domain)>0:
                domainSet = []
                domainSet.append(obj)
                domainSet.append(field.name)
                domainSet.append(field.domain)
                domainAssociations.append(domainSet)
                print "Attempting to remove domain [" + field.domain + "] from field [" + field.name + "] in object [" + obj + "]..."
                arcpy.RemoveDomainFromField_management(obj, field.name)

    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)

def updateDomains():
    try:
        print "Scoping globals..."
        #global sdeRail
        global sdeDDev
        global ConsultantPM_txt
        global VTransPM_txt
        global Consultants_txt
        global ConsultantsContact_txt
        global ProjectType_txt
        global LocationType_txt
        global VRLID_join_csv
        global AssetType_txt
        global AllPMs_txt
        global ProjectDescription_txt

#Disassociating domains from fields
        print "Disconnecting domains from fields..."
        disconnectDomains(sdeDDev + "/PROJ_AddProject_WebFC")
        disconnectDomains(sdeDDev + "/PROJ_Projects")
        disconnectDomains(sdeDDev + "/PROJ_StatusUpdate_WebFC")
        disconnectDomains(sdeDDev + "/PROJ_StatusUpdates")

#Delete domains
        print "Deleting domains..."
        domains = arcpy.da.ListDomains(sdeDDev)
        for domain in domains:
            if "ConsultantPM" in domain.name:
                arcpy.DeleteDomain_management(sdeDDev, domain.name)
            elif "VTransPM" in domain.name:
                arcpy.DeleteDomain_management(sdeDDev, domain.name)
            elif "Consultants" in domain.name:
                arcpy.DeleteDomain_management(sdeDDev, domain.name)
            elif "ConsultantContact" in domain.name:
                arcpy.DeleteDomain_management(sdeDDev, domain.name)
            elif "RailLine" in domain.name:
                arcpy.DeleteDomain_management(sdeDDev, domain.name)
            elif "AssetType" in domain.name:
                arcpy.DeleteDomain_management(sdeDDev, domain.name)
            elif "LocType" in domain.name:
                arcpy.DeleteDomain_management(sdeDDev, domain.name)
            elif "ProjectType" in domain.name:
                arcpy.DeleteDomain_management(sdeDDev, domain.name)
            elif "AllPMs" in domain.name:
                arcpy.DeleteDomain_management(sdeDDev, domain.name)
            elif "ProjDescript" in domain.name:
                arcpy.DeleteDomain_management(sdeDDev, domain.name)
            elif "ProjectName" in domain.name:
                arcpy.DeleteDomain_management(sdeDDev, domain.name)

        print "Recreating domains..."
        arcpy.TableToDomain_management(ConsultantPM_txt, "CODE", "DESCRIPTION", sdeDDev, "ConsultantPM", "Consultant Project Managers", "REPLACE")
        arcpy.TableToDomain_management(VTransPM_txt, "CODE", "DESCRIPTION", sdeDDev, "VTransPM", "VTrans Project Managers", "REPLACE")
        arcpy.TableToDomain_management(Consultants_txt, "CODE", "DESCRIPTION", sdeDDev, "Consultants", "Design Consultants", "REPLACE")
        arcpy.TableToDomain_management(ConsultantsContact_txt, "CODE", "DESCRIPTION", sdeDDev, "ConsultantContact", "Consultant Contact Info", "REPLACE")
        arcpy.TableToDomain_management(VRLID_join_csv, "RailLineCode", "RailLineDescription", sdeDDev, "RailLine", "Rail Line", "REPLACE")
        arcpy.TableToDomain_management(AssetType_txt, "CODE", "DESCRIPTION", sdeDDev, "AssetType", "Asset Type", "REPLACE")
        arcpy.TableToDomain_management(LocationType_txt, "CODE", "DESCRIPTION", sdeDDev, "LocType", "Project Location Type (Point, Line, Multi)", "REPLACE")
        arcpy.TableToDomain_management(ProjectType_txt, "CODE", "DESCRIPTION", sdeDDev, "ProjectType", "Project Type", "REPLACE")
        arcpy.TableToDomain_management(AllPMs_txt, "CODE", "DESCRIPTION", sdeDDev, "AllPMs", "All Project Managers", "REPLACE")
        arcpy.TableToDomain_management(ProjectDescription_txt, "CODE", "DESCRIPTION", sdeDDev, "ProjDescript", "Basic Project Description", "REPLACE")

        connSource = adodbapi.connect(RailConn)
        csrSource = connSource.cursor()
        csrSource.execute("SELECT DISTINCT ProjectName FROM [GDB_DDev].[DDev_ADMIN].[PROJ_Projects] WHERE ProjectName IS NOT NULL UNION SELECT DISTINCT ProjectName FROM [GDB_DDev].[DDev_ADMIN].[PROJ_AddProject_WebFC] WHERE ProjectName IS NOT NULL")
        lstSource = csrSource.fetchall()
        csrSource.close()

        arcpy.CreateDomain_management(sdeDDev, "ProjectName", "VTrans Project Name", "TEXT", "CODED")
        
        for rowSource in lstSource:
             arcpy.AddCodedValueToDomain_management(sdeDDev, "ProjectName", rowSource[0], rowSource[0])
                
        print "Sorting coded value domains..."
        arcpy.SortCodedValueDomain_management(sdeDDev, "VTransPM", "CODE", "ASCENDING")
        arcpy.SortCodedValueDomain_management(sdeDDev, "Consultants", "CODE", "ASCENDING")
        arcpy.SortCodedValueDomain_management(sdeDDev, "ConsultantContact", "CODE", "ASCENDING")
        arcpy.SortCodedValueDomain_management(sdeDDev, "ProjectType", "CODE", "ASCENDING")
        arcpy.SortCodedValueDomain_management(sdeDDev, "RailLine", "CODE", "ASCENDING")
        arcpy.SortCodedValueDomain_management(sdeDDev, "AssetType", "CODE", "ASCENDING")
        arcpy.SortCodedValueDomain_management(sdeDDev, "AllPMs", "CODE", "ASCENDING")
        arcpy.SortCodedValueDomain_management(sdeDDev, "ProjDescript", "CODE", "ASCENDING")
        arcpy.SortCodedValueDomain_management(sdeDDev, "ConsultantPM", "CODE", "ASCENDING")
        arcpy.SortCodedValueDomain_management(sdeDDev, "LocType", "CODE", "ASCENDING")
        arcpy.SortCodedValueDomain_management(sdeDDev, "ProjectName", "CODE", "ASCENDING")

        print "Reassociating fields with their domains..."
        for dom in domainAssociations:
            arcpy.AssignDomainToField_management(dom[0], dom[1], dom[2])

    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)

def main():
    try:
        global startTime
        print "Begin main subroutine..."

        CalcVRLIDs()
        dynSegAddProjects()
        #statusUpdatesAppend()
        dynSegStatusUpdates()
        projStatusRelates()
        #updateDomains()
        
#Calculating processing time, completing process
        endTime = datetime.datetime.now()
        execTime = endTime - startTime
        outTime = divmod(execTime.days * 86400 + execTime.seconds, 60)
        print "Elapsed time = " + str(outTime[0]) + " minute(s) " + str(outTime[1]) + " second(s)"
        print "Process complete."

    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)
                    
    finally:   
        print "Finally done!"

if __name__ == "__main__":
    main()

