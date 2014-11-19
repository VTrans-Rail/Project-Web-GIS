# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# 4_Status Table Relate.py
# Created on: 2014-11-19 09:45:05.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Set the necessary product code
import arceditor


# Import arcpy module
import arcpy


# Local variables:
Project_Lines_FC = "Database Connections\\GDB_Rail.sde\\GDB_Rail.RAIL_ADMIN.PROJ_Lines"
Project_Point_FC = "Database Connections\\GDB_Rail.sde\\GDB_Rail.RAIL_ADMIN.PROJ_Points"
Project_Status_Table = "Database Connections\\GDB_Rail.sde\\GDB_Rail.RAIL_ADMIN.PROJ_StatusUpdates"
GDB_Rail_RAIL_ADMIN_PROJ_Points_PROJ_StatusUpdates = "Database Connections\\GDB_Rail.sde\\GDB_Rail.RAIL_ADMIN.PROJ_Points_PROJ_StatusUpdates"
GDB_Rail_RAIL_ADMIN_PROJ_Lines_PROJ_StatusUpdates = "Database Connections\\GDB_Rail.sde\\GDB_Rail.RAIL_ADMIN.PROJ_Lines_PROJ_StatusUpdates"

# Process: Point-Status relationship
arcpy.CreateRelationshipClass_management(Project_Point_FC, Project_Status_Table, GDB_Rail_RAIL_ADMIN_PROJ_Points_PROJ_StatusUpdates, "SIMPLE", "GDB_Rail.RAIL_ADMIN.PROJ_StatusUpdates", "GDB_Rail.RAIL_ADMIN.PROJ_Points", "NONE", "ONE_TO_MANY", "NONE", "ProjectName", "ProjectName", "", "")

# Process: Line-Status relationship
arcpy.CreateRelationshipClass_management(Project_Lines_FC, Project_Status_Table, GDB_Rail_RAIL_ADMIN_PROJ_Lines_PROJ_StatusUpdates, "SIMPLE", "GDB_Rail.RAIL_ADMIN.PROJ_StatusUpdates", "GDB_Rail.RAIL_ADMIN.PROJ_Lines", "NONE", "ONE_TO_MANY", "NONE", "ProjectName", "ProjectName", "", "")

