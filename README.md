# d3-save-svg

 A fork of the nytimes [svg-crowbar](http://nytimes.github.io/svg-crowbar/) bookmarklet that extracts SVG nodes and accompanying styles from an HTML document and downloads them as an SVG file --- A file which you could open and edit in Adobe Illustrator, for instance. Because SVGs are resolution independent, it’s great for when you want to use web technologies to create documents that are meant to be printed (like, maybe on newsprint). It was created with [d3.js](https://d3js.org) in mind, but it should work fine no matter how you choose to generate your SVG.

[Project page](http://edeno.github.com/d3-save-svg/)

### Differences from the bookmarklet
+  Can use to download specific svg, which can be incorporated into buttons for exporting images. See example on the [project page](http://edeno.github.com/d3-save-svg/).
+  Allows specification of custom file names.
+  Handles embedded raster images.
+  Has convenience method for embedding raster images.

### Note
Most of this has been cobbled together from stackoverflow and issues logged on the nytimes svg-crowbar repo.

### API

#### d3_save_svg.save(svgElement, config)
Given a SVG element and an optional configuration object, `save` embeds external CSS styling and downloads the file. The filename will be (in order of existence) the svgElement ID, the svgElement class, or the window title. Optionally, you can specify the filename in the config object such that `config.filename` will be the name of the downloaded file.

#### d3_save_svg.embedRasterImages(imageElement)
A convenience function for converting a referenced raster image to base64 data via data URI, so that it is embedded in the SVG. This ensures that the downloaded image will contain the raster image. Probably should be updated to just directly convert a referenced link to data URI instead of doing it in two separate steps.

### Contributing
`npm install` to get the development dependencies, test and build.

Testing is via [Tape](https://github.com/substack/tape) and [jsdom](https://github.com/tmpvar/jsdom). Right now the tests are pretty rudimentary. Also `index.html` serves as a good check on whether things are working.

Development is done using the [git-flow](http://nvie.com/posts/a-successful-git-branching-model/) workflow. Please merge changes into the `develop` branch.

See [CONTRIBUTING.md](/CONTRIBUTING.md) for additional information.
