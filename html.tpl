<div class="jimu-popup-window" style="display: none;">
    <div id="impa-modal" class="modal" tabindex="-1" data-backdrop="static" data-keyboard="false" style="display: none;">
        <form id=“$TABLENAME” class="form-horizontal" action="${action}" method="post">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true"></button>
                    <h3>${title}</h3>
                </div>
                <div class="modal-body">
<code>
                    <div class="control-group">
                        <label for="$NAME" class="control-label">中文名称</label>
                        <div class="controls">
                            <input id="$NAME" name="$NAME" type="text" placeholder="名称" value=“${$TABLENAME.$NAME!}"/>
                        </div>
                    </div>
</code>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" onclick="$('#impa').ajaxLoad();">提交</button>
                    <button type="button" data-dismiss="modal" class="btn btn-primary">关闭</button>
                </div>   
            </div>
        </form>

    </div>
</div>