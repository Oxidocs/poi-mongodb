var gulp = require ('gulp');
var plumber = require('gulp-plumber');
var notify = require('gulp-notify');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var uglifycss = require('gulp-uglifycss');
var bs = require('browser-sync').create();

var plumberErrorHandler = {erroHandler: notify.onError({
  title:'Gulp',
  message: 'Error: <%= error.message %>'
})
};

gulp.task('sass', function(){
  gulp.src('./front/sass/**/*.scss')
    .pipe(plumber(plumberErrorHandler))
    .pipe(sass())
    .pipe(autoprefixer('last 2 versions'))
    .pipe(gulp.dest('./front/css'))
    .pipe(bs.reload({stream: true}));
  });

  gulp.task('browser-sync', function(){
    bs.init({
      proxy: "localhost:8000"
    });
  });

  gulp.task('watch', function(){
    gulp.watch('./front/sass/**/*.scss', ['sass']);
  });

  gulp.task('watch', ['browser-sync'], function(){
    gulp.watch('./front/sass/**/*.scss', ['sass']);
    gulp.watch('../templates/**/*.html').on('change',bs.reload);
  });


gulp.task('default',['sass', 'watch'])

// tareas build


gulp.task('css', function(){
  gulp.src('./front/css/*.css')
    .pipe(uglifycss({
      "maxLineLen":80,
      "uglyComments":true
    }))
    .pipe(gulp.dest('../static/front/css'))
});

gulp.task('js', function(){
  gulp.src('./front/js/*.js')
    .pipe(gulp.dest('../static/front/js'))
});

gulp.task('images',function(){
  gulp.src('./front/img/**/*.{png,jpg,gif,svg}')
    // .pipe(imagemin({
    //   optimizationLevel:7,
    //   progressive:true
    // }))
    .pipe(gulp.dest('../static/front/img'))
});

gulp.task('fonts', function(){
  gulp.src('./front/fonts/**')
    .pipe(gulp.dest('../static/front/fonts'))
})

gulp.task('rs-plugins', function(){
  gulp.src('./front/rs-plugin/**')
    .pipe(gulp.dest('../static/front/rs-plugin'))
})

gulp.task('build',['css', 'js', 'images', 'fonts', 'rs-plugins'])
