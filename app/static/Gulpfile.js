const gulp 			= require('gulp');
const browserify 	= require('browserify');
const source 		= require('vinyl-source-stream');
const buffer		= require('vinyl-buffer');
const babel 		= require('babelify');


gulp.task('scripts', ()=> {
	return browserify('./src/app.js')
		.on('error', handle_error)
		.transform(babel, {presets: ["react", "es2015"]}) 
		.bundle()
		.on('error', handle_error)
		.pipe(source('app.js'))
		.on('error', handle_error)
		.pipe(gulp.dest('./dist'))
});

gulp.task('watch', ()=> {
	gulp.watch('./src/**/*.js', ['scripts']);
})

function handle_error(err){
	console.error(err);
	this.emit('end');
}

gulp.task('default', ['scripts', 'watch']);