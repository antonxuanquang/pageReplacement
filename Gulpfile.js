var gulp  = require('gulp')
var shell = require('gulp-shell')
var watch = require('gulp-watch')

gulp.task('compile', shell.task([
	'clear',
	'python simpage.py < 1.txt',
]))

gulp.task('watch', function() {
	gulp.watch('./*.py', ['compile']);
});

gulp.task('default' ,function() {
	gulp.watch('./*.py', ['compile']);
});
