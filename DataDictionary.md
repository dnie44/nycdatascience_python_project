### Data Descriptions
| **Filename**     | **Description**                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------|
| bb_clean.csv     | Main product dataset. Already cleaned and binned.<br>  Also includes calculated attribute, bezel. |
| u_bought_raw.csv | "Viewed Ultimately Bought" dataset. <br> Up to 10 products for each sku in bb_clean.csv           |

### Data Type Table

#### filename: bb_clean.csv
| **attribute**  | **dtype** |
|----------------|-----------|
| sku  _[index]_ | int64     |
| color          | object    |
| curved         | bool      |
| display_type   | object    |
| energy_KWh     | float64   |
| height_nostand | float64   |
| manufacturer   | object    |
| model_num      | object    |
| model_year     | float64   |
| online_avail   | bool      |
| refresh_Hz     | float64   |
| regular_px     | float64   |
| resolution     | object    |
| review_average | float64   |
| review_count   | float64   |
| sale_px        | float64   |
| size_class     | object    |
| screen_size    | float64   |
| smart_capable  | bool      |
| store_avail    | bool      |
| sub_class      | object    |
| top_class      | object    |
| tv_name        | object    |
| warranty_yrs   | float64   |
| weight_nostand | float64   |
| width          | float64   |
| bezel          | float64   |

#### filename: u_bought_raw.csv
| **attribute** | **dtype** |
|---------------|-----------|
| sku  _[index]_| int64     |
| bu1           | float64   |
| bu2           | float64   |
| bu3           | float64   |
| bu4           | float64   |
| bu5           | float64   |
| bu6           | float64   |
| bu7           | float64   |
| bu8           | float64   |
| bu9           | float64   |
| bu10          | float64   |
