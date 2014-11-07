#Script Documentation

##0_Create Domains

References a set of simple CSV files that will create (or replace) current domain values

After creation (replacement), domains are sorted alphabetically for easy access

###Features Needed:
```
Right now the domains are set by the values in the CSV

It would be nice to have some of the domains drawn from a query of the data source

The biggest need would be projects that are "completed" from our perspective (gone to contract) will no longer need to be in the drop down because there are no more status updates

Same could apply to project managers and POC info 

We should double check with Schultz to get the parameters for this
```

##1_Create WebFC and Project Table

This mega-script creates 2 feature classes and a table

###AddProject WebFC

This is the feature class that drives the [Add Project](http://vtrans.maps.arcgis.com/home/item.html?id=e6b7696ea6744ca0818a799a15c88407) GeoForm

Fields:
1. 