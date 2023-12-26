#installing flask using pupet
package { 'flask':
  ensure   => 'installed',
  provider => 'pip3',
}
