# install flask from pip3 offcourse using puppet.
package { 'python3-pip':
  ensure => 'installed',
}

package { 'python3':
  ensure => 'installed',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => [Package['python3-pip'], Package['python3']],
}
