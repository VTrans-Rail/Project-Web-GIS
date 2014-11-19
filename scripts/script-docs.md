#Script Documentation

Here are all the tools I built to process GeoForms into GIS data for review in dashboards, maps, and reports.

Here is an approximation of the process:

![image](/img/Flowchart.png)

##Overview:

####One-Time Tasks
######And their approximate order
_Creation, data backup, merging, etc_
  
0_Create Domains  
1_Create WebFC and Project Table  
2_Create Status Update Table  
3_Merge_Projects_Backup_Table  
5_Enable_Tracking_Versioned  

####Repetitive Tasks  
6_AddProject Append Calc VRLID  
7_AddProject Join Calculate DynSeg

8_StatusUpdate_Append
7_AddProject Join Calculate DynSeg
4_Status Table Relate

*New: Update domains based on changes*


##0_Create Domains

References a set of simple CSV files that will create (or replace) current domain values

After creation (replacement), domains are sorted alphabetically for easy access

###Features Needed:
```
Right now the domains are set by the values in the CSV

It would be nice to have some of the domains drawn from a query of the data source

The biggest need would be projects that are "completed" from our perspective (gone to contract) 
will no longer need to be in the drop down because there are no more status updates

Same could apply to project managers and POC info 

We should double check with Schultz to get the parameters for this
```

##1_Create WebFC and Project Table

This mega-script creates 2 feature classes and a table

###Add Project WebFC

This is the feature class that drives the [Add Project](http://vtrans.maps.arcgis.com/home/item.html?id=e6b7696ea6744ca0818a799a15c88407) GeoForm

It is aimed at the VTrans project managers who manage projects

###Status Update WebFC

This is the shorter feature class that drives the [Status Update](http://vtrans.maps.arcgis.com/home/item.html?id=eae67051b1cf44dfaf33f7d627327a69) GeoForm.

It is aimed at our consultant project managers who give us updates to projects as the occur.

###Projects Table

This table is mostly the same as the **Add Project WebFC** with some fields expanded later in the **6_AddProject Append Calc VRLID** and **7_AddProject Join Calculate DynSeg** steps below

_AssetID_ is used to calculate _VRLID_

_VRLID_ expands into:
- LineName
- Operator
- Division
- Subdivision
- Branch
- StateOwned
- RailTrail

| Field                       | Description            | Domain                | Add Project WebFC           | Projects Table              | Status Update WebFC         |
| --------------------------- | ---------------------  | --------------------- | :-------------------------: | :-------------------------: | :-------------------------: |
| Project Name                | Project Name           |                       | :ballot_box_with_check:     | :ballot_box_with_check:     | :ballot_box_with_check:     |
| Project Type                | Project Type           | _ProjectType_         | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |
| Status Update               | Status Text            |                       |                             |                             | :ballot_box_with_check:     |
| PIN                         | PIN Number             |                       | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |
| Action Items                | Action Items           |                       |                             |                             | :ballot_box_with_check:     |
| VTrans PM                   | Internal PM            | _VTransPM_            | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |
| Latest Estimate             | Const. cost estimate   |                       |                             |                             |                             |
| Consultant PM               | External PM            | _ConsultantPM_        | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |
| Environmental All-Clear     | Env. All-Clear         | _Boolean_             | :ballot_box_with_check:     | :ballot_box_with_check:     | :ballot_box_with_check:     |
| Consultant                  | Consultant Company     | _Consultants_         | :ballot_box_with_check:     |                             | :ballot_box_with_check:     |
| Utility Clearance           | Util. Clearance        | _Boolean_             | :ballot_box_with_check:     | :ballot_box_with_check:     | :ballot_box_with_check:     |
| Consultance Contact         | Contact info           | _ConsultantContact_   | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |
| ROW Clearance               | ROW Clearance          | _Boolean_             | :ballot_box_with_check:     | :ballot_box_with_check:     | :ballot_box_with_check:     |
| Rail Line (VRLID proxy)     | Rail Line (Abbrev.)    | _RailLine_            | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |
| Railroad Clearance          | RR Clearance           | _Boolean_             | :ballot_box_with_check:     | :ballot_box_with_check:     | :ballot_box_with_check:     |
| FromMP                      | Starting MP            |                       | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |
| Advertise Target            | Project start date     |                       | :ballot_box_with_check:     | :ballot_box_with_check:     | :ballot_box_with_check:     |
| VRLID                       | VRLID                  |                       | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |
| ToMP                        | Ending MP              |                       | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |
| Updating PM                 | Who did the update     | _AllPMs_              |                             | :ballot_box_with_check:     |                             |
| Line Name                   | Line abbreviation      |                       |                             | :ballot_box_with_check:     |                             |
| Asset Type                  | Asset Type             | _AssetType_           | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |
| created_user                | (for edit tracking)    |                       | :ballot_box_with_check:     |                             | :ballot_box_with_check:     |
| Operator                    | Rail operator          |                       |                             |                             | :ballot_box_with_check:     |
| AssetID                     | Asset ID (system)      |                       | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |
| created_date                | (for edit tracking)    |                       | :ballot_box_with_check:     |                             | :ballot_box_with_check:     |
| Division                    | Rail division          |                       |                             |                             | :ballot_box_with_check:     |
| Location Type               | Point, multi-point etc | _LocType_             | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |
| last_edited_user            | (for edit tracking)    |                       | :ballot_box_with_check:     |                             | :ballot_box_with_check:     |
| Subdivision                 | Rail subdivision       |                       | :ballot_box_with_check:     |                             | :ballot_box_with_check:     |
| Asset Number                | Br. Num, Xing Num      |                       | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |
| created_date                | (for edit tracking)    |                       |                             |                             | :ballot_box_with_check:     |
| Branch                      | Railroad branch        |                       |                             | :ballot_box_with_check:     |                             |
| Baisc Project Description   | For reports            | _ProjDescript_        | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |
| State Owned                 | Is state owned?        | _Boolean_             |                             | :ballot_box_with_check:     |                             |
| Full project description    | Long description       |                       | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |
| Rail Trail                  | Is rail trail?         | _Boolean_             |                             | :ballot_box_with_check:     |                             |
| Include                     | Include in reports     | _Boolean_             | :ballot_box_with_check:     | :ballot_box_with_check:     |                             |


##2_Create Status Update Table

This table will take the fields from the **Status Update WebFC** and add:

- VRLID
- FromMP
- ToMP


Which are required for dyn-segging

##3_Merge_Projects_Backup_Table

I have a backup copy of the projects table with the existing projects (as of 9/29) in a GDB. This moves the data into the SDE table after re-building

##4_Status Table Relate

This relates the dyn-segged **Projects FC's** (Points & Lines) to the **Status_Update** Table

This seems like it's a little out of place, but remember that most times the feature classes are already created and are appended by this whole process. 

##5_Enable_Tracking_Versioned

This registers as versioned and enables editor tracking on the following datasets. 

- Projects table
- StatusUpdate WebFC
- Status Update Table
- AddProject WebFC

This was done as a separate step because they never executed properly in the same model the created the feature classes

##6_AddProject Append Calc VRLID

Appends projects added from the **Add Project WebFC** from the GeoForm to the **Projects table**.

Then it calculates the _VRLID_ field based on the provided _AssetID_

###Features Needed
```
Case where there is no AssetID given (in error)
Case where there is no AssetID given (none exists)
```

##7_AddProject Join Calculate DynSeg

Takes the **Projects Table** and expands the _VRLID_ into:

- LineName
- Operator
- Division
- Subdivision
- Branch
- StateOwned
- RailTrail

Creates a QueryTable to split the table into Points and Lines

###Features Needed
```
Case: multi-point
Case: multi-line
```

Dyn-seggs each query table

Exports them to **PROJ_Lines** and **PROJ_Points**

Adds EditorTracking fields because the model tool won't add them
- created_user
- created_date
- last_edited_user
- last_edited_date

Updates the domain based on the added project

Deletes all rows from the **AddProject WebFC** so that next time duplicates won't get imported

##8_StatusUpdate_Append

Appends any status updates from the **StatusUpdate WebFC** to the **Status_Table**

##9_StatusUpdate_DynSeg

Dyn-seggs the project status updates so they can be analyzed in Operations Dashboard

Joins **Status Update** table to **Projects** table 

Calculates _VRLID, FromMP, ToMP_

Makes a table view to split out lines and points

###Features Needed
```
Case: multi-point
Case: multi-line
```

Dyn-seggs points and lines

Exports events to feature classes:

- **PROJ_StatusLines**
- **PROJ_StatusPoints**


###Overall Features Needed
```
Testing to ensure the process is robust
Automation - either on demand, hourly, or nightly runs
Reporting - either on demand, hourly, or nightly report/spreadsheet exports that the PMs could review 
    (they want to see previous updates)
Could either of these be geoprocessing services they could run themselves?
CaSe TeStInG - Convert to Proper Case or ALL CAPS
Custom domains - PMs filter out their projects for updates
Map out how to locate (dyn seg) the projects to simplify data entry
- Minimum entries - Just AssetID? What if none exist? Asset type/number/MP?
Removing "done" projects - needs definition from Schultz
Embed the forms in an easy-to-access website

Automated error reporting 
- Missing key values
- MPs out of range

User error reporting
- "I messed up a submission, please delete/update/fix"
- "I forgot to put something in"

Wishlist:
VPINS integration? Project names, PIN numbers, contact information, or other data extracts? Dates? Costs?
"Presentation Mode" - synchronize map views to remote PMs
```
