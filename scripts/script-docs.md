#Script Documentation

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

|           Field           |     Description     |        Domain       |    Add Project WebFC    |      Projects Table     |   Status Update WebFC   |
|---------------------------|---------------------|---------------------|-------------------------|-------------------------|-------------------------|
| Project Name              | Project Name        |                     | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: |
| Project Type              | Project Type        | _ProjectType_       | :ballot_box_with_check: | :ballot_box_with_check: |                         |
| Status Update             | Status Text         |                     |                         |                         | :ballot_box_with_check: |
| PIN                       | PIN Number          |                     | :ballot_box_with_check: | :ballot_box_with_check: |                         |
| Action Items              | Action Items        |                     |                         |                         | :ballot_box_with_check: |
| VTrans PM                 | Internal PM         | _VTransPM_          | :ballot_box_with_check: | :ballot_box_with_check: |                         |
| Latest Estimate           | Latest construction |                     |                         |                         |                         |
|                           | cost estimate       |                     |                         |                         | :ballot_box_with_check: |
|---------------------------|---------------------|---------------------|-------------------------|-------------------------|-------------------------|
| Consultant PM             | External PM         | _ConsultantPM_      | :ballot_box_with_check: | :ballot_box_with_check: |                         |
| Environmental All-Clear   | Env. All-Clear      | _Boolean_           | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: |
| Consultant                | Consultant Company  | _Consultants_       | :ballot_box_with_check: |                         | :ballot_box_with_check: |
| Utility Clearance         | Util. Clearance     | _Boolean_           | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: |
| Consultance Contact       | Contact info        | _ConsultantContact_ | :ballot_box_with_check: | :ballot_box_with_check: |                         |
| ROW Clearance             | ROW Clearance       | _Boolean_           | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: |
| Rail Line (VRLID proxy)   | Rail Line (Abbrev.) | _RailLine_          | :ballot_box_with_check: | :ballot_box_with_check: |                         |
| Railroad Clearance        | RR Clearance        | _Boolean_           | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: |
| FromMP                    | Starting MP         |                     | :ballot_box_with_check: | :ballot_box_with_check: |                         |
| Advertise Target          | Project start date  |                     | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: |
| VRLID                     | VRLID               |                     | :ballot_box_with_check: | :ballot_box_with_check: |                         |
| ToMP                      | Ending MP           |                     | :ballot_box_with_check: | :ballot_box_with_check: |                         |
| Updating PM               | Who did the update  | _AllPMs_            |                         | :ballot_box_with_check: |                         |
| Line Name                 | Line abbreviation   |                     |                         | :ballot_box_with_check: |                         |
| Asset Type                | Asset Type          | _AssetType_         | :ballot_box_with_check: | :ballot_box_with_check: |                         |
| created_user              | (for edit tracking) |                     | :ballot_box_with_check: |                         | :ballot_box_with_check: |
| Operator                  | Rail operator       |                     |                         |                         | :ballot_box_with_check: |
| AssetID                   | Asset ID (system)   |                     | :ballot_box_with_check: | :ballot_box_with_check: |                         |
| created_date              | (for edit tracking) |                     | :ballot_box_with_check: |                         | :ballot_box_with_check: |
| Division                  | Rail division       |                     |                         |                         | :ballot_box_with_check: |
| Location Type             | Point, multi-point, |                     |                         |                         |                         |
|                           | line, multi-line    | _LocType_           | :ballot_box_with_check: | :ballot_box_with_check: |                         |
|---------------------------|---------------------|---------------------|-------------------------|-------------------------|-------------------------|
| last_edited_user          | (for edit tracking) |                     | :ballot_box_with_check: |                         | :ballot_box_with_check: |
| Subdivision               | Rail subdivision    |                     | :ballot_box_with_check: |                         | :ballot_box_with_check: |
| Asset Number              | Br. Num, Xing Num   |                     | :ballot_box_with_check: | :ballot_box_with_check: |                         |
| created_date              | (for edit tracking) |                     |                         |                         | :ballot_box_with_check: |
| Branch                    | Railroad branch     |                     |                         | :ballot_box_with_check: |                         |
| Baisc Project Description | For reports         | _ProjDescript_      | :ballot_box_with_check: | :ballot_box_with_check: |                         |
| State Owned               | Is state owned?     | _Boolean_           |                         | :ballot_box_with_check: |                         |
| Full project description  | Long description    |                     | :ballot_box_with_check: | :ballot_box_with_check: |                         |
| Rail Trail                | Is rail trail?      | _Boolean_           |                         | :ballot_box_with_check: |                         |
| Include                   | Include in reports  | _Boolean_           | :ballot_box_with_check: | :ballot_box_with_check: |                         |