var fs = require('fs');
var ini = require('ini');
var config = ini.parse(fs.readFileSync('./locations.ini', 'utf-8'))
console.log(config);
module.exports = function (grunt) {

    var grunt_conf_obj = {
        pkg: grunt.file.readJSON('package.json'),
        copy: {
            css: {
                files: [
                    // includes files within path and its sub-directories
                    {
                        expand: true,
                        cwd: 'build/release/css',
                        src: ['front_landing.css'],
                        dest: config.ae_landing_app_location + '/css'
                    }
                ]
            }
        },
        watch: {
            css: {
                files: ['css/**/*.less', 'css/**/*.css'],
                tasks: ['less', 'copy:css']
            }
        },

        less: {
            dev: {
                files: {
                    "build/release/css/front_landing.css": "css/front_landing.less"
                }
            }
        }

    };

    grunt.initConfig(grunt_conf_obj);

    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-bower-concat');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-less');


    grunt.registerTask('styles', ['less']);
    grunt.registerTask('test', ['jshint', 'qunit']);

    grunt.registerTask('default', ['less', 'copy:css']);

};
