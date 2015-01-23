"""
Rail Projects Initial Build - This script initializes the system for processing status updates created by consultant/contractors in order to create a history.
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
            DDEV_PROJ_Status_Updates__Table_ = sdeDDev + "/" + line[line.index("= \"")+3:len(line)-2]
            #print DDEV_PROJ_Status_Updates__Table_
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
        elif "RailConn" in line:
                    RailConn = line[line.index("= \"")+3:len(line)-2]
                    #print RailConn
        else:
            pass

        domainAssociations = []

def compressDB():
    try:
        print "Compressing database..."    
#disconnect any users
        arcpy.DisconnectUser(sdeDDev,"ALL")

#first statistics update
        arcpy.AnalyzeDatasets_management(sdeDDev, "SYSTEM", "", "ANALYZE_BASE","ANALYZE_DELTA","ANALYZE_ARCHIVE")
    
#compress database
        arcpy.Compress_management(sdeDDev)

#second statistics update
        arcpy.AnalyzeDatasets_management(sdeDDev, "SYSTEM", "", "ANALYZE_BASE","ANALYZE_DELTA","ANALYZE_ARCHIVE")            

    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)            


def disconnectDomains(obj):
    try:
        global domainAssociations
#Remove domains from their associated fields.  Domains association with fields prevent those domains from being deleted.
        fields = arcpy.ListFields(obj)
        for field in fields:
            #desc = arcpy.Describe(field)
            if len(field.domain)>0:
                if "_1" not in field.domain:
                    domainSet = []
                    domainSet.append(obj)
                    domainSet.append(field.name)
                    domainSet.append(field.domain)
                    domainAssociations.append(domainSet)
                #print "Attempting to remove domain [" + field.domain + "] from field [" + field.name + "] in object [" + obj + "]..."
                arcpy.RemoveDomainFromField_management(obj, field.name)
    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)

def createDomains():
    try:
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

        arcpy.env.workspace = sdeDDev

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

#Compress database to clear up transaction activity related to domain deletions
        compressDB()

#Create domains
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
        csrSource.execute("SELECT DISTINCT ProjectName FROM [GDB_DDev].[DDev_ADMIN].[PROJ_Projects] WHERE ProjectName IS NOT NULL")
        lstSource = csrSource.fetchall()
        csrSource.close()

        arcpy.CreateDomain_management(sdeDDev, "ProjectName", "VTrans Project Name", "TEXT", "CODED")
        
        for rowSource in lstSource:
             arcpy.AddCodedValueToDomain_management(sdeDDev, "ProjectName", rowSource[0], rowSource[0])

#Sort domains
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

    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)

def createStatusUpdateTable():
    try:
        global DDEV_PROJ_Status_Updates__Table_
        global DDEV_Status_Update_WebFC            
        
        if arcpy.Exists(DDEV_PROJ_Status_Updates__Table_):
            print "Existing Project Status Update table found.  Deleting existing table..."
            arcpy.Delete_management(DDEV_PROJ_Status_Updates__Table_)

        print "Creating Status Update Table..."        
# Process: Create Table (2)
        arcpy.CreateTable_management(sdeDDev, "PROJ_StatusUpdates", DDEV_Status_Update_WebFC, "")

        print "Adding Fields..."
# Process: Add Field (77)
        arcpy.AddField_management(DDEV_PROJ_Status_Updates__Table_, "VRLID", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field (78)
        arcpy.AddField_management(DDEV_PROJ_Status_Updates__Table_, "FromMP", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field (79)
        arcpy.AddField_management(DDEV_PROJ_Status_Updates__Table_, "ToMP", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        
    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)

def createAndMergeProjectsBackupTable():
    try:
        global DDEV_Projects_Table
        global sdeDDev
        global dev_gdb_Projects_Backup
            
        fieldMapping = (dev_gdb_Projects_Backup + "ProjectName \"Project Name\" true true false 100 Text 0 0 ,First,#,,ProjectName,-1,-1;" + 
                        dev_gdb_Projects_Backup + "ProjectType \"ProjectType\" true true false 255 Text 0 0 ,First,#,,ProjectType,-1,-1;" + 
                        dev_gdb_Projects_Backup + "PIN \"PIN Number\" true true false 7 Text 0 0 ,First,#,,PIN,-1,-1;" + 
                        dev_gdb_Projects_Backup + "VTransPM \"VTrans Project Manager\" true true false 255 Text 0 0 ,First,#,,VTransPM,-1,-1;" + 
                        dev_gdb_Projects_Backup + "ConsultantPM \"Consultant Project Manager\" true true false 255 Text 0 0 ,First,#,,ConsultantPM,-1,-1;" + 
                        dev_gdb_Projects_Backup + "Consultant \"Consultant\" true true false 255 Text 0 0 ,First,#,,Consultant,-1,-1;" + 
                        dev_gdb_Projects_Backup + "ConsultantPMContact \"Consultant PM Contact Info\" true true false 250 Text 0 0 ,First,#,,ConsultantPMContact,-1,-1;" + 
                        dev_gdb_Projects_Backup + "RailLine \"Rail Line\" true true false 255 Text 0 0 ,First,#,,RailLine,-1,-1;" + 
                        dev_gdb_Projects_Backup + "VRLID \"VRLID\" true true false 255 Text 0 0 ,First,#,,VRLID,-1,-1;" + 
                        dev_gdb_Projects_Backup + "LineName \"Line Name\" true true false 255 Text 0 0 ,First,#,,LineName,-1,-1;" + 
                        dev_gdb_Projects_Backup + "Operator \"Operator\" true true false 255 Text 0 0 ,First,#,,Operator,-1,-1;" + 
                        dev_gdb_Projects_Backup + "Division \"Division\" true true false 255 Text 0 0 ,First,#,,Division,-1,-1;" + 
                        dev_gdb_Projects_Backup + "Subdivision \"Subdivision\" true true false 255 Text 0 0 ,First,#,,Subdivision,-1,-1;" +
                        dev_gdb_Projects_Backup + "Branch \"Branch\" true true false 255 Text 0 0 ,First,#,,Branch,-1,-1;" + 
                        dev_gdb_Projects_Backup + "StateOwned \"State Owned\" true true false 255 Text 0 0 ,First,#,,StateOwned,-1,-1;" + 
                        dev_gdb_Projects_Backup + "RailTrail \"Rail Trail\" true true false 255 Text 0 0 ,First,#,,RailTrail,-1,-1;" + 
                        dev_gdb_Projects_Backup + "FromMP \"FromMP\" true true false 8 Double 8 38 ,First,#,,FromMP,-1,-1;" + 
                        dev_gdb_Projects_Backup + "ToMP \"ToMP\" true true false 8 Double 8 38 ,First,#,,ToMP,-1,-1;" + 
                        dev_gdb_Projects_Backup + "AssetType \"Asset Type\" true true false 255 Text 0 0 ,First,#,,AssetType,-1,-1;" + 
                        dev_gdb_Projects_Backup + "AssetID \"AssetID\" true true false 255 Text 0 0 ,First,#,,AssetID,-1,-1;" + 
                        dev_gdb_Projects_Backup + "LocationType \"Location Type\" true true false 255 Text 0 0 ,First,#,,LocationType,-1,-1;" + 
                        dev_gdb_Projects_Backup + "AssetNumber \"Asset Number\" true true false 255 Text 0 0 ,First,#,,AssetNumber,-1,-1;" + 
                        dev_gdb_Projects_Backup + "BasicDescription \"Basic Project Description\" true true false 250 Text 0 0 ,First,#,,BasicDescription,-1,-1;" + 
                        dev_gdb_Projects_Backup + "ProjectDescription \"Full Project Description\" true true false 500 Text 0 0 ,First,#,,ProjectDescription,-1,-1;" + 
                        dev_gdb_Projects_Backup + "LatestConstEst \"Latest Construction Estimate w/ E&C\" true true false 8 Double 8 38 ,First,#,,LatestConstEst,-1,-1;" + 
                        dev_gdb_Projects_Backup + "EnvAllClear \"Environmental All Clear\" true true false 255 Text 0 0 ,First,#,,EnvAllClear,-1,-1;" + 
                        dev_gdb_Projects_Backup + "UtilClear \"Utilities Clearance\" true true false 255 Text 0 0 ,First,#,,UtilClear,-1,-1;" + 
                        dev_gdb_Projects_Backup + "ROWClear \"ROW Clearance\" true true false 255 Text 0 0 ,First,#,,ROWClear,-1,-1;" + 
                        dev_gdb_Projects_Backup + "RRClear \"Railroad Clearance\" true true false 255 Text 0 0 ,First,#,,RRClear,-1,-1;" + 
                        dev_gdb_Projects_Backup + "AdvertiseTarget \"Project Advertisement Target\" true true false 255 Text 0 0 ,First,#,,AdvertiseTarget,-1,-1;" + 
                        dev_gdb_Projects_Backup + "Include \"Include In Reports\" true true false 255 Text 0 0 ,First,#,,Include,-1,-1;" + 
                        dev_gdb_Projects_Backup + "created_user \"created_user\" true true false 255 Text 0 0 ,First,#,,created_user,-1,-1;" + 
                        dev_gdb_Projects_Backup + "created_date \"created_date\" true true false 36 Date 0 0 ,First,#,,created_date,-1,-1;" + 
                        dev_gdb_Projects_Backup + "last_edited_user \"last_edited_user\" true true false 255 Text 0 0 ,First,#,,last_edited_user,-1,-1;" + 
                        dev_gdb_Projects_Backup + "last_edited_date \"last_edited_date\" true true false 36 Date 0 0 ,First,#,,last_edited_date,-1,-1")
        
        print "Merging Projects Backup Table into development Projects table..."
        arcpy.Append_management(dev_gdb_Projects_Backup, DDEV_Projects_Table, "NO_TEST",fieldMapping, "")

    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)

def enableVersionTracking():
    try:
        global DDEV_Add_Project_WebFC
        global DDEV_Status_Update_WebFC

        print "Enabling editor tracking..."
        arcpy.EnableEditorTracking_management(DDEV_Projects_Table, "created_user", "created_date", "last_edited_user", "last_edited_date", "", "UTC")
        arcpy.EnableEditorTracking_management(DDEV_Status_Update_WebFC, "created_user", "created_date", "last_edited_user", "last_edited_date", "", "UTC")
        arcpy.EnableEditorTracking_management(DDEV_Add_Project_WebFC, "created_user", "created_date", "last_edited_user", "last_edited_date", "", "UTC")
        arcpy.EnableEditorTracking_management(DDEV_PROJ_Status_Updates__Table_, "created_user", "created_date", "last_edited_user", "last_edited_date", "", "UTC")

        print "Registering key tables as versioned for editor tracking..."
        arcpy.RegisterAsVersioned_management(DDEV_Projects_Table, "NO_EDITS_TO_BASE")
        arcpy.RegisterAsVersioned_management(DDEV_Status_Update_WebFC, "NO_EDITS_TO_BASE")
        arcpy.RegisterAsVersioned_management(DDEV_PROJ_Status_Updates__Table_, "NO_EDITS_TO_BASE")
        arcpy.RegisterAsVersioned_management(DDEV_Add_Project_WebFC, "NO_EDITS_TO_BASE")
        
    except Exception, msg:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
        print(fname, exc_tb.tb_lineno, msg)


def main():
    try:
        print "Begin main subroutine..."
        
        global startTime
        global domainAssociations
        global sdeRail
        global sdeDDev
        global RAIL_Status_Update_WebFC
        global RAIL_Status_Update_WebFC
        global DDEV_Projects_Table
        global RAIL_Projects_Table
        global DDEV_Add_Project_WebFC
        global RAIL_Add_Project_WebFC
        
#Copying existing tables from production.
        if arcpy.Exists(DDEV_Status_Update_WebFC):
            #print "Existing Project Status Update feature class found.  Deleting existing feature class..."
            arcpy.Delete_management(DDEV_Status_Update_WebFC)

        #print "Copying production status update feature class to development..."
        arcpy.FeatureClassToGeodatabase_conversion(RAIL_Status_Update_WebFC,sdeDDev)

        if arcpy.Exists(DDEV_Projects_Table):
            #print "Existing Project table found.  Deleting existing table..."
            arcpy.Delete_management(DDEV_Projects_Table)
            
        #print "Copying production Project table to development..."
        arcpy.TableToGeodatabase_conversion(RAIL_Projects_Table,sdeDDev)

        if arcpy.Exists(DDEV_Add_Project_WebFC):
            #print "Existing Project table found.  Deleting existing table..."
            arcpy.Delete_management(DDEV_Add_Project_WebFC)
            
        #print "Copying production Project table to development..."
        arcpy.env.transferDomains = False
        arcpy.FeatureClassToGeodatabase_conversion(RAIL_Add_Project_WebFC,sdeDDev)

        createDomains()
        createStatusUpdateTable()
        createAndMergeProjectsBackupTable()
        enableVersionTracking()

        print "Reassociating fields with their domains..."
        for dom in domainAssociations:
            print dom[0] + ":  Reassociating domain \'" + dom[2] + "\' with field \'" + dom[1] + "\'"
            arcpy.AssignDomainToField_management(dom[0], dom[1], dom[2])

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
