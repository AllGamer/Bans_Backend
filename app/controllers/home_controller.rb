class HomeController < ApplicationController
layout "bansui"
  def index
    @posts = Post.all
    respond_to do |format|
      format.html # index.html.erb
      format.xml  { render :xml => @posts }
    end
  end

  def about
    respond_to do |format|
      format.html # about.html.erb
    end
  end

  def downloads
    respond_to do |format|
      format.html # downloads.html.erb
    end
  end
end
