class ApiController < ApplicationController
  def index
  end
  
  def heartbeat
   if params[:apikey] == nil
	render :text => "FAIL {'error':{'no apikey given'}}", :status => 503 and return
   end
   @apikey=params[:apikey]
   @server=Server.find(:first, :conditions => ["apikey = ?", @apikey])
   if @apikey == nil
      render :text => "FAIL {'error':{'apikey not authorized'}}", :status => 503 and return
   else
      @server.update_attributes(:last_heartbeat => Time.now)
      render :text => "OK\n"+ @server.to_json
   end
  end
end
