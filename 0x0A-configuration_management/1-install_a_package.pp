# This Puppet manifest installs Flask version 2.1.0 and Werkzeug 2.0.3 using pip3.
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['Werkzeug'],
}

package { 'Werkzeug':
  ensure   => '2.0.3',
  provider => 'pip3',
}
