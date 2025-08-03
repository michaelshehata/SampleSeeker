import supabase from './database.js'

async function createTables() {
  const { data, error } = await supabase
    .from('users')
    .insert([{ username: 'testuser' }])

  if (error) {
    console.error('Error inserting data:', error)
  } else {
    console.log('Inserted data:', data)
  }
}

createTables()
