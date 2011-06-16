class CreateServers < ActiveRecord::Migration
  def self.up
    create_table :servers do |t|
      t.string :apikey
      t.string :last_heartbeat
      t.string :known_server_ip

      t.timestamps
    end
  end

  def self.down
    drop_table :servers
  end
end
