# Image-Formatting-Server
## Sample GET Request
`curl http://localhost:5000/api/format-image\?image-url\=http://www.python.org/static/community_logos/python-logo-master-v3-TM.png\&height\=150\&width\=800\&left\=100\&top\=50\&right\=400\&bottom\=150\&filters\=find_edges,sharpen,blur`

## Parameter Description
| Parameter     | Description                   | Can be passed independently   | Sample Value |
| ------------- |:-----------------------------:|:-----------------------------:|:------------:|
| image-url     | URL pointing to image         | Yes                           | http://www.python.org/static/community_logos/python-logo-master-v3-TM.png
| height        | Rezised height of image       | Yes                           | 150
| width         | Rezised width of image        | Yes                           | 800
| left          | X-value of first crop point   | No (need top/right/bottom)    | 100
| top           | Y-value of first crop point   | No (need left/right/bottom)   | 50
| right         | X-value of second crop point  | No (need top/left/bottom)     | 400
| bottom        | Y-value of second crop point  | No (need top/right/left)      | 150
| filters       | <sup>*</sup> List of filters  | No (need top/right/left)      | find_edges,sharpen,blur
<sup>*</sup> Valid filters are blur, contour, detail, edge_enhance, edge_enhance_more, emboss, find_edges, sharpen, smooth, and smooth_more. Multiple filters must be seperated by commas.

## Git Branching Convention
Git branches are named using the following template:

`<issue number>/<description-of-issue>`