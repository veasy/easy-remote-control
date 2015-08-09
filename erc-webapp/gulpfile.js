var gulp = require('gulp');
var bower = require('bower');
var concat = require('gulp-concat');
var sass = require('gulp-sass');
var minifyCss = require('gulp-minify-css');
var rename = require('gulp-rename');

var paths = {
  watch: [
    "./www/modules/**/*.scss",
    "./www/modules/**/*.js"
  ]
};

gulp.task('default', ['sass', 'js']);

gulp.task("sass", function(done) {
  gulp.src("./www/modules/sauerkraut/main/scss/all.scss")
      .pipe(sass({
        errLogToConsole: true
      }))
      .pipe(minifyCss({
        keepSpecialComments: 0
      }))
      .pipe(rename("sauerkraut.min.css" ))
      .pipe(gulp.dest("./www/compiled/css/"))
      .on("end", done);
});

gulp.task("js", function(done) {
  gulp.src([
    "./resources/js/app.js",
    "./resources/js/controllers.js",
    "./resources/js/directives.js",
    "./resources/js/services.js"
  ])
  .pipe(concat("erc-webapp.min.js", {sep: ""}))
  .pipe(gulp.dest("./resources/compiled/js/"))
  .on("end", done);
});

gulp.task("watch", function() {
  gulp.watch(paths.watch, ["sass", "js"]);
});

