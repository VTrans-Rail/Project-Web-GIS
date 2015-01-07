"""
Rail Projects Post Process- This script adds the VRLID to project status updates.
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

print "beginning script..."

startTime = datetime.datetime.now()

with open("C://Connections.txt","r") as Conn:
    lines = Conn.readlines()

for line in lines:
    if line[0:1]!="#":
        if "sdeDDev = " in line:
            sdeDDev = line[line.index("= \"")+3:len(line)-2]
            print sdeDDev
        elif "sdeRail = " in line:
            sdeRail = line[line.index("= \"")+3:len(line)-2]
            print sdeRail
        elif "ConsultantPM_txt" in line:
            ConsultantPM_txt = line[line.index("= \"")+3:len(line)-2]
            print ConsultantPM_txt
        elif "VTransPM_txt" in line:
            VTransPM_txt = line[line.index("= \"")+3:len(line)-2]
            print VTransPM_txt
        elif "Consultants_txt" in line:
            Consultants_txt = line[line.index("= \"")+3:len(line)-2]
            print Consultants_txt
        elif "ConsultantsContact_txt" in line:
            ConsultantsContact_txt = line[line.index("= \"")+3:len(line)-2]
            print ConsultantsContact_txt
        elif "ProjectType_txt" in line:
            ProjectType_txt = line[line.index("= \"")+3:len(line)-2]
            print ProjectType_txt
        elif "LocationType_txt" in line:
            LocationType_txt = line[line.index("= \"")+3:len(line)-2]
            print LocationType_txt            
        elif "VRLID_join_csv" in line:
            VRLID_join_csv = line[line.index("= \"")+3:len(line)-2]
            print VRLID_join_csv
        elif "AssetType_txt" in line:
            AssetType_txt = line[line.index("= \"")+3:len(line)-2]
            print AssetType_txt
        elif "AllPMs_txt" in line:
            AllPMs_txt = line[line.index("= \"")+3:len(line)-2]
            print AllPMs_txt
        elif "ProjectDescription_txt" in line:
            ProjectDescription_txt = line[line.index("= \"")+3:len(line)-2]
            print ProjectDescription_txt
        elif "Status_Update_WebFC" in line:
            DDEV_Status_Update_WebFC = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            RAIL_Status_Update_WebFC = sdeRail + "/" + line[line.index("= \"")+3:len(line)-2]
            print DDEV_Status_Update_WebFC
            print RAIL_Status_Update_WebFC
        elif "PROJ_Status_Updates__Table_" in line:
            DDEV_PROJ_Status_Updates__Table_ = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            print DDEV_PROJ_Status_Updates__Table_
        elif "dev_gdb_Projects_Backup" in line:
            dev_gdb_Projects_Backup = line[line.index("= \"")+3:len(line)-2]
            print dev_gdb_Projects_Backup
        elif "GDB_Projects_Table" in line:
            DDEV_Projects_Table = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            RAIL_Projects_Table = sdeRail + "/" + line[line.index("= \"")+3:len(line)-2]
            print DDEV_Projects_Table
            print RAIL_Projects_Table
        elif "Add_Project_WebFC" in line:
            DDEV_Add_Project_WebFC = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            RAIL_Add_Project_WebFC = sdeRail + "/" + line[line.index("= \"")+3:len(line)-2]
            print DDEV_Add_Project_WebFC
            print RAIL_Add_Project_WebFC            
        elif "PROJ_Projects_View1" in line:
            DDEV_PROJ_Projects_View1 = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            print DDEV_PROJ_Projects_View1
        elif "PROJ_Projects_View2" in line:
            DDEV_PROJ_Projects_View2 = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            print DDEV_PROJ_Projects_View2
        elif "AssetID" in line:
            RAIL_AssetID = sdeRail + "/" + line[line.index("= \"")+3:len(line)-2]
            print RAIL_AssetID
        elif "PROJ_Projects_View3" in line:
            DDEV_PROJ_Projects_View3 = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            print DDEV_PROJ_Projects_View3
        else:
            pass


def CalcVRLIDs():
    try:
# Local variables:
        global DDEV_Add_Project_WebFC
        global DDEV_Projects_Table
        global DDEV_AssetID
        global DDEV_PROJ_Projects_View1
        global DDEV_PROJ_Projects_View2
        global DDEV_PROJ_Projects_View3

        fieldInfo = ("OBJECTID OBJECTID VISIBLE NONE;Shape Shape VISIBLE NONE;" + 
                    "ProjectName ProjectName VISIBLE NONE;" + 
                    "ProjectType ProjectType VISIBLE NONE;" + 
                    "PIN PIN VISIBLE NONE;" + 
                    "VTransPM VTransPM VISIBLE NONE;" + 
                    "ConsultantPM ConsultantPM VISIBLE NONE;" + 
                    "Consultant Consultant VISIBLE NONE;" + 
                    "ConsultantPMContact ConsultantPMContact VISIBLE NONE;" + 
                    "RailLine RailLine VISIBLE NONE;" + 
                    "FromMP FromMP VISIBLE NONE;" + 
                    "ToMP ToMP VISIBLE NONE;" + 
                    "AssetType AssetType VISIBLE NONE;" + 
                    "AssetID AssetID VISIBLE NONE;" + 
                    "LocationType LocationType VISIBLE NONE;" + 
                    "AssetNumber AssetNumber VISIBLE NONE;" + 
                    "BasicDescription BasicDescription VISIBLE NONE;" + 
                    "ProjectDescription ProjectDescription VISIBLE NONE;" + 
                    "LatestConstEst LatestConstEst VISIBLE NONE;" + 
                    "EnvAllClear EnvAllClear VISIBLE NONE;" + 
                    "UtilClear UtilClear VISIBLE NONE;" + 
                    "ROWClear ROWClear VISIBLE NONE;" + 
                    "RRClear RRClear VISIBLE NONE;" + 
                    "AdvertiseTarget AdvertiseTarget VISIBLE NONE;" + 
                    "Include Include VISIBLE NONE;" + 
                    "created_user created_user VISIBLE NONE;" + 
                    "created_date created_date VISIBLE NONE;" + 
                    "last_edited_user last_edited_user VISIBLE NONE;" + 
                    "last_edited_date last_edited_date VISIBLE NONE")

# Process: Add Project web fc table view
        arcpy.MakeTableView_management(DDEV_Add_Project_WebFC, DDEV_PROJ_Projects_View1, "", "", fieldInfo)


        fieldMapping = ("ProjectName \"Project Name\" true true false 100 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,ProjectName,-1,-1;" + 
                        "ProjectType \"ProjectType\" true true false 255 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,ProjectType,-1,-1;" + 
                        "PIN \"PIN Number\" true true false 7 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,PIN,-1,-1;" + 
                        "VTransPM \"VTrans Project Manager\" true true false 255 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,VTransPM,-1,-1;" + 
                        "ConsultantPM \"Consultant Project Manager\" true true false 255 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,ConsultantPM,-1,-1;" + 
                        "Consultant \"Consultant\" true true false 255 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,Consultant,-1,-1;" + 
                        "ConsultantPMContact \"Consultant PM Contact Info\" true true false 250 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,ConsultantPMContact,-1,-1;" +
                        "RailLine \"Rail Line\" true true false 255 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,RailLine,-1,-1;" + 
                        "VRLID \"VRLID\" true true false 255 Text 0 0 ,First,#;" + 
                        "LineName \"Line Name\" true true false 255 Text 0 0 ,First,#;" +
                        "Operator \"Operator\" true true false 255 Text 0 0 ,First,#;" + 
                        "Division \"Division\" true true false 255 Text 0 0 ,First,#;" + 
                        "Subdivision \"Subdivision\" true true false 255 Text 0 0 ,First,#;" + 
                        "Branch \"Branch\" true true false 255 Text 0 0 ,First,#;" + 
                        "StateOwned \"State Owned\" true true false 255 Text 0 0 ,First,#;" + 
                        "RailTrail \"Rail Trail\" true true false 255 Text 0 0 ,First,#;" + 
                        "FromMP \"FromMP\" true true false 8 Double 8 38 ,First,#,DDEV_PROJ_Projects_View1,FromMP,-1,-1;" + 
                        "ToMP \"ToMP\" true true false 8 Double 8 38 ,First,#,DDEV_PROJ_Projects_View1,ToMP,-1,-1;" + 
                        "AssetType \"Asset Type\" true true false 255 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,AssetType,-1,-1;" + 
                        "AssetID \"AssetID\" true true false 255 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,AssetID,-1,-1;" + 
                        "LocationType \"Location Type\" true true false 255 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,LocationType,-1,-1;" + 
                        "AssetNumber \"Asset Number\" true true false 255 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,AssetNumber,-1,-1;" + 
                        "BasicDescription \"Basic Project Description\" true true false 250 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,BasicDescription,-1,-1;" + 
                        "ProjectDescription \"Full Project Description\" true true false 500 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,ProjectDescription,-1,-1;" + 
                        "LatestConstEst \"Latest Construction Estimate w/ E&C\" true true false 8 Double 8 38 ,First,#,DDEV_PROJ_Projects_View1,LatestConstEst,-1,-1;" + 
                        "EnvAllClear \"Environmental All Clear\" true true false 255 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,EnvAllClear,-1,-1;" + 
                        "UtilClear \"Utilities Clearance\" true true false 255 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,UtilClear,-1,-1;" + 
                        "ROWClear \"ROW Clearance\" true true false 255 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,ROWClear,-1,-1;" + 
                        "RRClear \"Railroad Clearance\" true true false 255 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,RRClear,-1,-1;" + 
                        "AdvertiseTarget \"Project Advertisement Target\" true true false 255 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,AdvertiseTarget,-1,-1;" + 
                        "Include \"Include In Reports\" true true false 255 Text 0 0 ,First,#,DDEV_PROJ_Projects_View1,Include,-1,-1")

# Process: Append add project to project table
        arcpy.Append_management(DDEV_PROJ_Projects_View1, DDEV_Projects_Table, "NO_TEST", fieldMapping, "")

        fieldInfo = ("OBJECTID OBJECTID VISIBLE NONE;" + 
                    "ProjectName ProjectName VISIBLE NONE;" + 
                    "ProjectType ProjectType VISIBLE NONE;" + 
                    "PIN PIN VISIBLE NONE;" + 
                    "VTransPM VTransPM VISIBLE NONE;" + 
                    "ConsultantPM ConsultantPM VISIBLE NONE;" + 
                    "Consultant Consultant VISIBLE NONE;" + 
                    "ConsultantPMContact ConsultantPMContact VISIBLE NONE;" +
                    "RailLine RailLine VISIBLE NONE;VRLID VRLID VISIBLE NONE;" + 
                    "LineName LineName VISIBLE NONE;" + 
                    "Operator Operator VISIBLE NONE;" + 
                    "Division Division VISIBLE NONE;" + 
                    "Subdivision Subdivision VISIBLE NONE;" + 
                    "Branch Branch VISIBLE NONE;" + 
                    "StateOwned StateOwned VISIBLE NONE;" +
                    "RailTrail RailTrail VISIBLE NONE;" + 
                    "FromMP FromMP VISIBLE NONE;" + 
                    "ToMP ToMP VISIBLE NONE;" + 
                    "AssetType AssetType VISIBLE NONE;" + 
                    "AssetID AssetID VISIBLE NONE;" + 
                    "LocationType LocationType VISIBLE NONE;" + 
                    "AssetNumber AssetNumber VISIBLE NONE;" + 
                    "BasicDescription BasicDescription VISIBLE NONE;" + 
                    "ProjectDescription ProjectDescription VISIBLE NONE;" + 
                    "LatestConstEst LatestConstEst VISIBLE NONE;" + 
                    "EnvAllClear EnvAllClear VISIBLE NONE;" + 
                    "UtilClear UtilClear VISIBLE NONE;" + 
                    "ROWClear ROWClear VISIBLE NONE;" + 
                    "RRClear RRClear VISIBLE NONE;" + 
                    "AdvertiseTarget AdvertiseTarget VISIBLE NONE;" + 
                    "Include Include VISIBLE NONE;" + 
                    "created_user created_user VISIBLE NONE;" + 
                    "created_date created_date VISIBLE NONE;" + 
                    "last_edited_user last_edited_user VISIBLE NONE;"
                    "last_edited_date last_edited_date VISIBLE NONE")

# Process: project table view
        arcpy.MakeTableView_management(DDEV_Projects_Table, DDEV_PROJ_Projects_View2, "", "", fieldInfo)

# Process: join to asset ID
        arcpy.AddJoin_management(DDEV_PROJ_Projects_View2, "AssetID", RAIL_AssetID, "AssetID", "KEEP_COMMON")

# Process: calculate VRLID
        arcpy.CalculateField_management(DDEV_PROJ_Projects_View2, "VRLID", "[GDB_Rail.RAIL_ADMIN.ASSET_ID_SCHEMA.VRLID]", "VB", "")

    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)

def main():
    try:
        global startTime
        print "Begin main subroutine..."

        CalcVRLIDs()

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

