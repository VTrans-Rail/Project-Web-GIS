"""
Rail Projects - This script will process status updates created by consultant/contractors in order to create a history.
It is based on a series of scripts exported from Model Builder.

Created/Updated By: Rick Scott
Create Date: 12/11/2014

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
            Status_Update_WebFC = sdeRail + "/" + line[line.index("= \"")+3:len(line)-2]
            print Status_Update_WebFC
        elif "PROJ_Status_Updates__Table_" in line:
            PROJ_Status_Updates__Table_ = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            print PROJ_Status_Updates__Table_
        else:
            pass

###set up global SDE connections
###sdeRail = "C:/BatchJobs/SDEConnections/GDB_Rail(Rail_Admin).sde"
###sdeDDev = "C:/BatchJobs/SDEConnections/AOTGISTST01-GDB_DDev(WIN).sde"
##sdeDDev = "C:/BatchJobs/SDEConnections/AOTGISTST01-GDB_DDev(DDev_Admin).sde"
###sdeDDev = "C:/BatchJobs/SDEConnections/AOTGISTST01-GDB_DDev(VTrans_Admin).sde"
##
###Initialize global variables
##ConsultantPM_txt = "V:\\Projects\\Specials\\Rail_Inventory_and_Condition\\_dev\\ProjectsWeb\\script\\ConsultantPM.txt"
##VTransPM_txt = "V:\\Projects\\Specials\\Rail_Inventory_and_Condition\\_dev\\ProjectsWeb\\script\\VTransPM.txt"
##Consultants_txt = "V:\\Projects\\Specials\\Rail_Inventory_and_Condition\\_dev\\ProjectsWeb\\script\\Consultants.txt"
##ConsultantsContact_txt = "V:\\Projects\\Specials\\Rail_Inventory_and_Condition\\_dev\\ProjectsWeb\\script\\ConsultantsContact.txt"
##ProjectType_txt = "V:\\Projects\\Specials\\Rail_Inventory_and_Condition\\_dev\\ProjectsWeb\\script\\ProjectType.txt"
##LocationType_txt = "V:\\Projects\\Specials\\Rail_Inventory_and_Condition\\_dev\\ProjectsWeb\\script\\LocationType.txt"
##VRLID_join_csv = "V:\\Projects\\Specials\\Rail_Inventory_and_Condition\\_dev\\ProjectsWeb\\script\\VRLID-join.csv"
##AssetType_txt = "V:\\Projects\\Specials\\Rail_Inventory_and_Condition\\_dev\\ProjectsWeb\\script\\AssetType.txt"
##AllPMs_txt = "V:\\Projects\\Specials\\Rail_Inventory_and_Condition\\_dev\\ProjectsWeb\\script\\AllPMs.txt"
##ProjectDescription_txt = "V:\\Projects\\Specials\\Rail_Inventory_and_Condition\\_dev\\ProjectsWeb\\script\\ProjectDescription.txt"

def createDomains():
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

        print "Creating domains..."
        # Process: Table To Domain
        arcpy.TableToDomain_management(ConsultantPM_txt, "CODE", "DESCRIPTION", sdeDDev, "ConsultantPM", "Consultant Project Managers", "REPLACE")

        # Process: Table To Domain (2)
        arcpy.TableToDomain_management(VTransPM_txt, "CODE", "DESCRIPTION", sdeDDev, "VTransPM", "VTrans Project Managers", "REPLACE")

        # Process: Table To Domain (3)
        arcpy.TableToDomain_management(Consultants_txt, "CODE", "DESCRIPTION", sdeDDev, "Consultants", "Design Consultants", "REPLACE")

        # Process: Table To Domain (4)
        arcpy.TableToDomain_management(ConsultantsContact_txt, "CODE", "DESCRIPTION", sdeDDev, "ConsultantContact", "Consultant Contact Info", "REPLACE")

        # Process: Table To Domain (5)
        arcpy.TableToDomain_management(VRLID_join_csv, "RailLineCode", "RailLineDescription", sdeDDev, "RailLine", "Rail Line", "REPLACE")

        # Process: Table To Domain (6)
        arcpy.TableToDomain_management(AssetType_txt, "CODE", "DESCRIPTION", sdeDDev, "AssetType", "Asset Type", "REPLACE")

        # Process: Table To Domain (7)
        arcpy.TableToDomain_management(LocationType_txt, "CODE", "DESCRIPTION", sdeDDev, "LocType", "Project Location Type (Point, Line, Multi)", "REPLACE")

        # Process: Table To Domain (9)
        arcpy.TableToDomain_management(ProjectType_txt, "CODE", "DESCRIPTION", sdeDDev, "ProjectType", "Project Type", "REPLACE")

        # Process: Table To Domain (10)
        arcpy.TableToDomain_management(AllPMs_txt, "CODE", "DESCRIPTION", sdeDDev, "AllPMs", "All Project Managers", "REPLACE")

        # Process: Table To Domain (8)
        arcpy.TableToDomain_management(ProjectDescription_txt, "CODE", "DESCRIPTION", sdeDDev, "ProjDescript", "Basic Project Description", "REPLACE")

        print "Sorting coded value domains..."
        # Process: Sort Coded Value Domain
        arcpy.SortCodedValueDomain_management(sdeDDev, "VTransPM", "CODE", "ASCENDING")

        # Process: Sort Coded Value Domain (2)
        arcpy.SortCodedValueDomain_management(sdeDDev, "Consultants", "CODE", "ASCENDING")

        # Process: Sort Coded Value Domain (3)
        arcpy.SortCodedValueDomain_management(sdeDDev, "ConsultantContact", "CODE", "ASCENDING")

        # Process: Sort Coded Value Domain (4)
        arcpy.SortCodedValueDomain_management(sdeDDev, "ProjectType", "CODE", "ASCENDING")

        # Process: Sort Coded Value Domain (5)
        arcpy.SortCodedValueDomain_management(sdeDDev, "RailLine", "CODE", "ASCENDING")

        # Process: Sort Coded Value Domain (6)
        arcpy.SortCodedValueDomain_management(sdeDDev, "AssetType", "CODE", "ASCENDING")

        # Process: Sort Coded Value Domain (7)
        arcpy.SortCodedValueDomain_management(sdeDDev, "AllPMs", "CODE", "ASCENDING")

        # Process: Sort Coded Value Domain (8)
        arcpy.SortCodedValueDomain_management(sdeDDev, "ProjDescript", "CODE", "ASCENDING")

        # Process: Sort Coded Value Domain (9)
        arcpy.SortCodedValueDomain_management(sdeDDev, "ConsultantPM", "CODE", "ASCENDING")

        # Process: Sort Coded Value Domain (10)
        arcpy.SortCodedValueDomain_management(sdeDDev, "LocType", "CODE", "ASCENDING")

    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)

def createStatusUpdateTable():
    try:

        if arcpy.Exists(PROJ_Status_Updates__Table_):
            print "Existing table found.  Deleting existing table..."
            arcpy.Delete_management(PROJ_Status_Updates__Table_)

        print "Creating Status Update Table..."        
        # Process: Create Table (2)
        arcpy.CreateTable_management(sdeDDev, "PROJ_StatusUpdates", Status_Update_WebFC, "")

        print "Adding Fields..."
        # Process: Add Field (77)
        arcpy.AddField_management(PROJ_Status_Updates__Table_, "VRLID", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: Add Field (78)
        arcpy.AddField_management(PROJ_Status_Updates__Table_, "FromMP", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: Add Field (79)
        arcpy.AddField_management(PROJ_Status_Updates__Table_, "ToMP", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        
    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)

def main():
    try:
        print "Begin main subroutine..."

        #createDomains()
        createStatusUpdateTable()

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
